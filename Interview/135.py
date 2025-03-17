from xml import etree

# Sample XML content
xml_content = """
<cXML payloadID="123456" timestamp="2023-01-01T12:00:00">
    <Header>
        <From>
            <Credential domain="DUNS">
                <Identity>123456789</Identity>
            </Credential>
        </From>
        <To>
            <Credential domain="DUNS">
                <Identity>987654321</Identity>
            </Credential>
        </To>
        <Sender>
            <Credential domain="DUNS">
                <Identity>567890123</Identity>
            </Credential>
            <UserAgent>ExampleAgent</UserAgent>
        </Sender>
    </Header>
    <Request>
        <OrderRequest>
            <OrderRequestHeader orderID="A12345" orderDate="2023-01-01">
                <Total>
                    <Money currency="USD">100.00</Money>
                </Total>
            </OrderRequestHeader>
        </OrderRequest>
    </Request>
</cXML>
"""

# Parse the XML content
root = etree.fromstring(xml_content)  # type: ignore

# Extract and print root attributes
payload_id = root.get("payloadID")
timestamp = root.get("timestamp")
print("Payload ID:", payload_id)
print("Timestamp:", timestamp)

# Extract and print Header information
from_identity = root.xpath("//From/Credential/Identity")[0].text
to_identity = root.xpath("//To/Credential/Identity")[0].text
sender_identity = root.xpath("//Sender/Credential/Identity")[0].text
user_agent = root.xpath("//Sender/UserAgent")[0].text
print("From Identity:", from_identity)
print("To Identity:", to_identity)
print("Sender Identity:", sender_identity)
print("User Agent:", user_agent)

# Extract and print OrderRequest information
order_request_headers = root.xpath("//OrderRequest/OrderRequestHeader")
for order_request_header in order_request_headers:
    order_id = order_request_header.get("orderID")
    order_date = order_request_header.get("orderDate")
    total_money = order_request_header.xpath(".//Money")[0].text
    currency = order_request_header.xpath(".//Money")[0].get("currency")

    # Print the extracted information for each OrderRequest
    print("\nOrder ID:", order_id)
    print("Order Date:", order_date)
    print("Total Money:", total_money)
    print("Currency:", currency)
