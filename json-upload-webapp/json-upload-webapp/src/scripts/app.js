document.getElementById('uploadButton').addEventListener('click', processFile);

function processFile() {
    const fileInput = document.getElementById('fileInput');
    const output = document.getElementById('output');

    if (fileInput.files.length === 0) {
        alert('Please select a file!');
        return;
    }

    const file = fileInput.files[0];
    const reader = new FileReader();

    reader.onload = function(event) {
        try {
            const json = JSON.parse(event.target.result);
            displayImportantInfo(json);
        } catch (error) {
            console.error('Error parsing JSON file:', error);
            output.textContent = 'Error parsing JSON file!';
        }
    };

    reader.readAsText(file);
}

function truncateUrl(url, maxLength = 30) {
    if (url.length <= maxLength) return url;
    const truncated = url.slice(0, maxLength) + '...';
    return truncated;
}

function displayImportantInfo(json) {
    const output = document.getElementById('output');
    const importantInfo = `
        <div class="section" id="observedAt" draggable="true">
            <strong>Observed At:</strong> ${json.observedAt || 'N/A'}<br><br>
        </div>
        <div class="section endpoint" id="endpoint" draggable="true">
            <strong>Endpoint:</strong><br>
            <div class="indent">
                <strong>Hostname:</strong> ${json.endpoint?.hostname || 'N/A'}<br>
                <strong>OS:</strong> ${json.endpoint?.os?.name || 'N/A'} (${json.endpoint?.os?.version || 'N/A'})<br>
                <strong>OS Kind:</strong> ${json.endpoint?.os?.kind || 'N/A'}<br>
            </div>
        </div>
        <div class="section feed" id="feed" draggable="true">
            <strong>Feed:</strong><br>
            <div class="indent">
                <strong>Region:</strong> ${json.feed?.region || 'N/A'}<br>
                <strong>Realm:</strong> ${json.feed?.realm || 'N/A'}<br>
            </div>
        </div>
        <div class="section activity" id="activity" draggable="true">
            <strong>Activity:</strong><br>
            <div class="indent">
                <strong>Trigger:</strong> ${json.activity?.trigger || 'N/A'}<br>
                <strong>Primary Category:</strong> ${json.activity?.primaryCategory || 'N/A'}<br>
                <strong>Categories:</strong> ${json.activity?.categories?.join(', ') || 'N/A'}<br>
            </div>
        </div>
        <div class="section process" id="process" draggable="true">
            <strong>Process:</strong><br>
            <div class="indent">
                <strong>Executable Name:</strong> ${json.process?.executable?.name || 'N/A'}<br>
                <strong>Executable Path:</strong> ${json.process?.executable?.path || 'N/A'}<br>
                <strong>Application Name:</strong> ${json.process?.application?.name || 'N/A'}<br>
                <strong>Application Description:</strong> ${json.process?.application?.description || 'N/A'}<br>
                <strong>Application Vendor:</strong> ${json.process?.application?.vendor || 'N/A'}<br>
            </div>
        </div>
        <div class="section ui" id="ui" draggable="true">
            <strong>UI:</strong><br>
            <div class="indent">
                <strong>Window Title:</strong> ${json.ui?.windows?.[0]?.title || 'N/A'}<br>
                <strong>Screenshot:</strong> <a href="${json.ui?.screenshots?.[0]?.links?.access?.href || '#'}" target="_blank">${truncateUrl(json.ui?.screenshots?.[0]?.links?.access?.href || 'N/A')}</a><br>
            </div>
        </div>
        <div class="section indicators" id="indicators" draggable="true">
            <strong>Indicators:</strong><br>
            <div class="indent">
                ${json.indicators?.map(indicator => `
                    <div class="item">
                        <strong>Indicator ID:</strong> ${indicator.id || 'N/A'}<br>
                        <strong>Indicator Kind:</strong> ${indicator.kind || 'N/A'}<br>
                        <strong>Matches:</strong> ${indicator.matches?.map(match => match.result?.value).join(', ') || 'N/A'}<br>
                    </div>
                `).join('') || 'N/A'}
            </div>
        </div>
        <div class="section resources" id="resources" draggable="true">
            <strong>Resources:</strong><br>
            <div class="indent">
                ${json.resources?.map(resource => `
                    <div class="item">
                        <strong>Kind:</strong> ${resource.kind || 'N/A'}<br>
                        <strong>Port:</strong> ${resource.port || 'N/A'}<br>
                        <strong>Scheme:</strong> ${resource.scheme || 'N/A'}<br>
                        <strong>URL:</strong> <a href="${resource.url || '#'}" target="_blank">${truncateUrl(resource.url || 'N/A')}</a><br>
                        <strong>Host:</strong> ${resource.host || 'N/A'}<br>
                        <strong>Path:</strong> ${resource.path || 'N/A'}<br>
                        ${resource._derivatives?.direction?.source?.path ? `<strong>Source Path:</strong> ${resource._derivatives.direction.source.path}<br>` : ''}
                        ${resource._derivatives?.direction?.source?.name ? `<strong>Source Name:</strong> ${resource._derivatives.direction.source.name}<br>` : ''}
                    </div>
                `).join('') || 'N/A'}
            </div>
        </div>
        <div class="section site" id="site" draggable="true">
            <strong>Site:</strong><br>
            <div class="indent">
                <strong>URL:</strong> <a href="${json.site?.url || '#'}" target="_blank">${truncateUrl(json.site?.url || 'N/A')}</a><br>
                <strong>Host:</strong> ${json.site?.host || 'N/A'}<br>
                <strong>Path:</strong> ${json.site?.path || 'N/A'}<br>
                <strong>Scheme:</strong> ${json.site?.scheme || 'N/A'}<br>
            </div>
        </div>
        <div class="section devices" id="devices" draggable="true">
            <strong>Devices:</strong><br>
            <div class="indent">
                <strong>Device ID:</strong> ${json.devices?.[0]?.id || 'N/A'}<br>
                <strong>Device Kind:</strong> ${json.devices?.[0]?.kind || 'N/A'}<br>
                <strong>Device Protocol:</strong> ${json.devices?.[0]?.protocol || 'N/A'}<br>
                <strong>Sync Product Name:</strong> ${json.devices?.[0]?.sync?.product?.name || 'N/A'}<br>
            </div>
        </div>
        <div class="section processing" id="processing" draggable="true">
            <strong>Processing:</strong><br>
            <div class="indent">
                <strong>Action Channel:</strong> ${json.processing?.actions?.[0]?.channel || 'N/A'}<br>
                <strong>Action Kind:</strong> ${json.processing?.actions?.[0]?.kind || 'N/A'}<br>
                <strong>Reason ID:</strong> ${json.processing?.actions?.[0]?.reasons?.[0]?.id || 'N/A'}<br>
                <strong>Reason Indicators:</strong> ${json.processing?.actions?.[0]?.reasons?.[0]?.indicators?.map(indicator => indicator.index).join(', ') || 'N/A'}<br>
            </div>
        </div>
        <div class="section user" id="user" draggable="true">
            <strong>User:</strong><br>
            <div class="indent">
                <strong>Username:</strong> ${json.user?.username || 'N/A'}<br>
                <strong>NetBIOS Domain:</strong> ${json.user?.netbiosDomain || 'N/A'}<br>
                <strong>Full Name:</strong> ${json.user?.fullname || 'N/A'}<br>
                <strong>Email:</strong> ${json.user?.email || 'N/A'}<br>
            </div>
        </div>
        <div class="section agent" id="agent" draggable="true">
            <strong>Agent:</strong><br>
            <div class="indent">
                <strong>Kind:</strong> ${json.agent?.kind || 'N/A'}<br>
                <strong>PID:</strong> ${json.agent?.pid || 'N/A'}<br>
                <strong>Version:</strong> ${json.agent?.version || 'N/A'}<br>
            </div>
        </div>
    `;
    output.innerHTML = importantInfo;
    makeSectionsDraggable();
    loadLayout();
}

function makeSectionsDraggable() {
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => {
        section.setAttribute('draggable', true);
        section.addEventListener('dragstart', dragStart);
        section.addEventListener('dragover', dragOver);
        section.addEventListener('drop', drop);
        section.addEventListener('dragenter', dragEnter);
        section.addEventListener('dragleave', dragLeave);
    });
    document.getElementById('output').addEventListener('dragover', dragOver);
    document.getElementById('output').addEventListener('drop', drop);
}

function dragStart(event) {
    event.dataTransfer.setData('text/plain', event.target.id);
    setTimeout(() => {
        event.target.classList.add('hide');
    }, 0);
}

function dragOver(event) {
    event.preventDefault();
    event.dataTransfer.dropEffect = 'move';
}

function dragEnter(event) {
    event.preventDefault();
    event.target.classList.add('drag-over');
}

function dragLeave(event) {
    event.target.classList.remove('drag-over');
}

function drop(event) {
    event.preventDefault();
    const id = event.dataTransfer.getData('text/plain');
    const draggable = document.getElementById(id);
    draggable.classList.remove('hide');
    event.target.classList.remove('drag-over');
    const dropzone = event.target.closest('.section');
    if (dropzone && dropzone !== draggable) {
        dropzone.parentNode.insertBefore(draggable, dropzone.nextSibling);
    } else {
        document.getElementById('output').appendChild(draggable);
    }
    saveLayout();
}

function saveLayout() {
    const sections = document.querySelectorAll('.section');
    const layout = Array.from(sections).map(section => section.id);
    localStorage.setItem('layout', JSON.stringify(layout));
}

function loadLayout() {
    const layout = JSON.parse(localStorage.getItem('layout'));
    if (layout) {
        const output = document.getElementById('output');
        layout.forEach(id => {
            const section = document.getElementById(id);
            if (section) {
                output.appendChild(section);
            }
        });
    }
}