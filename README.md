# databricks_connector_demo
Repository with manual and test code on purpose of tutorial how to connect with databricks cluster

## requirements

prepare your enviroment:
1. Install Python with version corresponding with cluaster you want to connect [link](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/databricks-connect#requirements)
2. "Venv" (Virtual environment) will help you separetes enviroments (or other e.g coda) [link](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-packages-using-pip-and-virtual-environments)
3. JRE need to be installed - for spark (sudo apt install default-jre)

## connect to databricks

![Configuration params from url](/image/configuration_from_link.png)

1. Create venv
2. Install databricks connector in corresponding with your cluster version 
```bash
pip install -U "databricks-connect==7.3.*")
```
3. Run 
```bash
databricks-connect configure
```
Provide all prompted info. All you can find in cluster link (above) and manual for personal tohen you can find [here](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/authentication#--generate-a-personal-access-token)
4. Test your connection
```bash
databricks-connect test
```