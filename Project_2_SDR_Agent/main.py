import asyncio
from agents.agent import run_sales_manager

if __name__ == "__main__":
    result = asyncio.run(run_sales_manager())
    print(result)
