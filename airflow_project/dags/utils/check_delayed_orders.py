import os
import yaml
import snowflake.connector
import sys

def load_snowflake_config():
    # find and load the Snowflake configuration from a YAML file
    config_path = os.path.join(os.path.dirname(__file__), '../config/snowflake_config.yaml')
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config('snowflake')

def main():
    # checks
    print("✅ Running Snowflake delayed orders check...")
    print("✅ Python path:", sys.executable)
    print("✅ Snowflake connector version:", snowflake.connector.__version__)

    # Main function to check for delayed orders in Snowflake
    sf_config = load_snowflake_config()

    try:
        # Establish connection to Snowflake
        conn = snowflake.connector.connect(
            user=sf_config['user'],
            password=sf_config['password'],
            account=sf_config['account'],
            warehouse=sf_config['warehouse'],
            database=sf_config['database'],
            schema=sf_config['schema'],
            role=sf_config['role'],
            login_timeout=20,
            client_session_keep_alive=False,
            ocsp_fail_open=True
        )
        print("✅ Successfully connected to Snowflake")

        # Execute the query to check for delayed orders
        cur = conn.cursor()
        cur.execute("""
            SELECT COUNT(*)
            FROM ECOMMERC_DB_ANALYTICS.ORDER_STATUS
            WHERE final_status = 'DELAYED';
        """)
        result = cur.fetchone()
        print("✅ Query Result:", result)
        cur.close()
        conn.close()

        # If there are delayed orders, raise an exception to fail the task in Airflow and send an alert email via Airflow
        if result is not None and result[0] > 0:
            raise Exception(f"⚠️ There are {result[0]} delayed orders found!")

    # Handle exceptions and print errors
    except Exception as e:
        print("❌ Error:", e)
        sys.exit(1) # Exit with a non-zero status to indicate failure

# Run the main function if this script is executed
if __name__ == "__main__":
    main()