from procrastinate import App, PsycopgConnector
from shared import Settings
import sys

config = Settings()
app = App(connector=PsycopgConnector(conninfo=config.database_url.encoded_string()))

if __name__ == "__main__":
    args = sys.argv[1:]
    po_working = args[0]
    with app.open():
        job = app.configure_task(name="create_sales_orders", queue="sap").defer(
            resume_url="http://slmething",
            po_working_path=po_working,
            va01_details={
                "order type": "ZWEO",
                "sales organization": 2200,
                "distribution channel": 10,
                "division": "00",
            },
            screen_order=[
                "VA01_INITIAL",
                "VA01_OVERVIEW",
                "VA01_SALES",
                "VA01_FAST_DATA_ENTRY",
                "HEADER_SALES",
                "HEADER_PARTNERS",
                "HEADER_ADD_DATA_A",
                {"name": "HEADER_ADD_DATA_B", "post_actions": {"type": "BACK"}},
            ],
        )
        print(job)
