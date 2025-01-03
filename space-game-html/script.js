/*****************************************
 * 全局 & DOM
 *****************************************/
const gameContainer = document.getElementById("game-container");
const player = document.getElementById("player");
const enemiesContainer = document.getElementById("enemies");
const lasersContainer = document.getElementById("lasers");
const enemyLasersContainer = document.getElementById("enemy-lasers");
const scoreBoard = document.getElementById("score-board");

// 变量
let playerX = 375;
let enemies = [];
let lasers = [];
let enemyLasers = [];
let enemyShooters = [];
let bulletCount = 5; // 当 bulletCount >= 5 时，发射白色子弹
let gameOver = false;
let score = 0;

// 用于给敌人分配唯一 id（若需更复杂的“独家锁定”可用它）
let nextEnemyId = 1;

/*****************************************
 * 敌人类型配置
 *****************************************/
const ENEMY_TYPE = {
    RED: {
        color: "red",
        scoreValue: 1,
        canShoot: false,
    },
    GREEN: {
        color: "green",
        scoreValue: 3,
        canShoot: true,
    },
};

/*****************************************
 * 键盘控制
 *****************************************/
document.addEventListener("keydown", (e) => {
    if (gameOver) return;

    if (e.key === "ArrowLeft" && playerX > 0) {
        playerX -= 20;
    } else if (e.key === "ArrowRight" && playerX < 750) {
        playerX += 20;
    } else if (e.key === " ") {
        shootLaser();
    }
    player.style.left = playerX + "px";
});

/*****************************************
 * 发射玩家子弹
 *****************************************/
function shootLaser() {
    // bulletCount >= 5 => 发射一颗白色子弹
    if (bulletCount >= 5) {
        const whiteLaser = document.createElement("div");
        whiteLaser.classList.add("laser", "white-laser");
        // 统一使用 bottom 定位，避免 top/bottom 冲突
        whiteLaser.style.left = (playerX + 22) + "px";
        whiteLaser.style.bottom = "60px";

        // 用 dataset 储存坐标
        whiteLaser.dataset.x = (playerX + 22).toString();
        whiteLaser.dataset.bottom = "60";

        lasersContainer.appendChild(whiteLaser);
        lasers.push(whiteLaser);
    } else {
        // 多发普通子弹
        const bulletSpacing = 20;
        const startX = playerX + 22 - (bulletCount - 1) * bulletSpacing / 2;

        for (let i = 0; i < bulletCount; i++) {
            const laser = document.createElement("div");
            laser.classList.add("laser");
            laser.style.left = (startX + i * bulletSpacing) + "px";
            laser.style.bottom = "60px";

            laser.dataset.x = (startX + i * bulletSpacing).toString();
            laser.dataset.bottom = "60";

            if (bulletCount === 1) {
                laser.dataset.angle = "0";
            } else {
                const middleIndex = Math.floor(bulletCount / 2);
                if (bulletCount % 2 === 1 && i === middleIndex) {
                    laser.dataset.angle = "0";
                } else {
                    const angle = (i - middleIndex) * 0.2;
                    laser.dataset.angle = angle.toString();
                }
            }
            lasersContainer.appendChild(laser);
            lasers.push(laser);
        }
    }
}

/*****************************************
 * 生成敌人
 *****************************************/
function spawnEnemy() {
    if (gameOver) return;

    // 30% 绿色敌人，其余红色
    const rand = Math.random();
    let type = ENEMY_TYPE.RED;
    if (rand < 0.3) {
        type = ENEMY_TYPE.GREEN;
    }

    const containerWidth = enemiesContainer.clientWidth;
    const enemyX = Math.random() * (containerWidth - 20);

    const enemyDiv = document.createElement("div");
    enemyDiv.classList.add("enemy", type.color);
    enemyDiv.style.left = enemyX + "px";
    enemyDiv.style.top = "0px";

    enemiesContainer.appendChild(enemyDiv);

    const enemy = {
        id: nextEnemyId++,
        x: enemyX,
        y: 0,
        width: 20,
        height: 20,
        element: enemyDiv,
        color: type.color,
        scoreValue: type.scoreValue,
    };
    enemies.push(enemy);

    if (type.canShoot) {
        enemyShooters.push({
            enemy: enemyDiv,
            lastShot: Date.now(),
        });
    }
}

/*****************************************
 * 移动敌人
 *****************************************/
function moveEnemies() {
    enemies.forEach((enemy, index) => {
        enemy.y += 2;
        enemy.element.style.top = enemy.y + "px";

        if (enemy.y > 600) {
            enemy.element.remove();
            removeEnemyByIndex(index);
        }
    });
}

/*****************************************
 * 敌人射击
 *****************************************/
function enemyShoot() {
    if (gameOver) return;
    const now = Date.now();
    const shootInterval = 2000;

    enemyShooters.forEach((shooter) => {
        const enemyRect = shooter.enemy.getBoundingClientRect();
        const containerRect = gameContainer.getBoundingClientRect();

        if (now - shooter.lastShot >= shootInterval) {
            const laser = document.createElement("div");
            laser.classList.add("enemy-laser");

            const x = enemyRect.left - containerRect.left + 8;
            const y = enemyRect.bottom - containerRect.top;

            laser.style.left = x + "px";
            laser.style.top = y + "px";

            laser.dataset.x = x.toString();
            laser.dataset.y = y.toString();

            enemyLasersContainer.appendChild(laser);
            enemyLasers.push(laser);

            shooter.lastShot = now;
        }
    });
}

/*****************************************
 * 敌人子弹移动(简单朝玩家)
 *****************************************/
function moveEnemyLasers() {
    enemyLasers.forEach((laser, index) => {
        let currentY = parseFloat(laser.dataset.y);
        let currentX = parseFloat(laser.dataset.x);

        const playerRect = player.getBoundingClientRect();
        const containerLeft = gameContainer.getBoundingClientRect().left;
        const playerCenterX = (playerRect.left - containerLeft) + 25;

        if (currentX < playerCenterX) currentX += 1;
        else if (currentX > playerCenterX) currentX -= 1;

        currentY += 4;
        laser.dataset.x = currentX.toString();
        laser.dataset.y = currentY.toString();

        laser.style.left = currentX + "px";
        laser.style.top = currentY + "px";

        if (currentY > gameContainer.clientHeight) {
            laser.remove();
            enemyLasers.splice(index, 1);
        }
    });
}

/*****************************************
 * 玩家子弹移动
 * -- 白色子弹向前追踪：只考虑敌人“在子弹上方”
 *****************************************/
function moveLasers() {
    lasers.forEach((laser, index) => {
        let laserX = parseFloat(laser.dataset.x);
        let laserBottom = parseFloat(laser.dataset.bottom);

        // --- 白色子弹 ---
        if (laser.classList.contains("white-laser")) {
            // 找到最近且 y >= bulletBottom 的敌人（不往回追）
            const nearest = findNearestEnemyAbove(laserX, laserBottom);
            if (nearest) {
                // 追踪
                const dx = nearest.x - laserX;
                const dy = nearest.y - laserBottom;
                const dist = Math.sqrt(dx * dx + dy * dy);
                const speed = 5;

                if (dist > 0) {
                    laserX += (dx / dist) * speed;
                    laserBottom += (dy / dist) * speed;
                }
            } else {
                // 没有敌人或都在下方 => 继续向上
                laserBottom += 5;
            }
        }
        // --- 普通子弹 ---
        else {
            const angle = parseFloat(laser.dataset.angle) || 0;
            laserBottom += 5; // 往上
            laserX += angle;  // 横向
        }

        // 更新坐标
        laser.dataset.x = laserX.toString();
        laser.dataset.bottom = laserBottom.toString();
        laser.style.left = laserX + "px";
        laser.style.bottom = laserBottom + "px";

        // 飞出屏幕则移除
        if (laserBottom > 600) {
            removeLaserByIndex(index);
        }
    });
}

/*****************************************
 * 只寻找子弹上方的最近敌人
 *****************************************/
function findNearestEnemyAbove(bulletX, bulletBottom) {
    let nearest = null;
    let minDist = Infinity;

    enemies.forEach((enemy) => {
        // 若敌人高于子弹
        if (enemy.y >= bulletBottom) {
            const dx = enemy.x - bulletX;
            const dy = enemy.y - bulletBottom;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < minDist) {
                minDist = dist;
                nearest = enemy;
            }
        }
    });
    return nearest;
}

/*****************************************
 * 碰撞检测
 *****************************************/
function checkCollisions() {
    // 玩家子弹 vs 敌人
    lasers.forEach((laser, laserIndex) => {
        const laserRect = laser.getBoundingClientRect();
        enemies.forEach((enemy, enemyIndex) => {
            const enemyRect = enemy.element.getBoundingClientRect();
            if (isColliding(laserRect, enemyRect)) {
                score += enemy.scoreValue;
                updateScore();

                enemy.element.remove();
                removeEnemyByIndex(enemyIndex);
                removeLaserByIndex(laserIndex);
            }
        });
    });

    // 敌人子弹 vs 玩家
    const playerRect = player.getBoundingClientRect();
    enemyLasers.forEach((enemyLaser, laserIndex) => {
        const laserRect = enemyLaser.getBoundingClientRect();
        if (isColliding(laserRect, playerRect)) {
            endGame();
        }
    });
}

/*****************************************
 * 工具函数：移除敌人
 *****************************************/
function removeEnemyByIndex(idx) {
    if (idx >= 0 && idx < enemies.length) {
        enemies[idx].element.remove();
        enemies.splice(idx, 1);
    }
}

/*****************************************
 * 工具函数：移除子弹
 *****************************************/
function removeLaserByIndex(idx) {
    if (idx >= 0 && idx < lasers.length) {
        lasers[idx].remove();
        lasers.splice(idx, 1);
    }
}

/*****************************************
 * 碰撞检测辅助
 *****************************************/
function isColliding(rect1, rect2) {
    return !(
        rect1.right < rect2.left ||
        rect1.left > rect2.right ||
        rect1.bottom < rect2.top ||
        rect1.top > rect2.bottom
    );
}

/*****************************************
 * 分数
 *****************************************/
function updateScore() {
    scoreBoard.textContent = "Score: " + score;
}

/*****************************************
 * 游戏结束
 *****************************************/
function endGame() {
    if (gameOver) return;
    gameOver = true;
    alert("Game Over! Score: " + score);
    window.location.reload();
}

/*****************************************
 * 初始化 & 主循环
 *****************************************/
function init() {
    // 每0.5秒生成一个敌人
    setInterval(spawnEnemy, 500);
    // 每0.5秒让绿色敌人射击一次
    setInterval(enemyShoot, 500);
    updateScore();
}

function gameLoop() {
    if (!gameOver) {
        moveEnemies();
        moveLasers();
        moveEnemyLasers();
        checkCollisions();
        requestAnimationFrame(gameLoop);
    }
}

// 启动游戏
init();
gameLoop();
