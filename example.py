from mysql.connector import connect
import psycopg2
from private_db_llm.config import LLMConfig
from private_db_llm.service import create_service

# 1. Open a MySQL connection
mysql_conn = connect(
    host="xxx", user="xxx", password="xxx", database="xxx"
)
postgres_conn = psycopg2.connect(
    host="xxx", user="xxx", password="xxx", database="xxx"
)

# 2. Configure LLM
llm_conf = LLMConfig(
    provider="openai",
    api_key="xxx",
    model="gpt-4o-mini"
)

# 3. Build service
svc = create_service(llm_conf)

# 4. Run with user prompt
result = svc.run(mysql_conn, "How many sales during the past 30 days?")
print(result)
