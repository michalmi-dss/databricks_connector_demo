# databricks_connector_demo
Repository with manual and test code on purpose of tutorial how to connect with databricks cluster

## requirements

prepare your enviroment:
1. Install Python with version corresponding with cluaster you want to connect [link](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/databricks-connect#requirements)
2. "Venv" (Virtual environment) will help you separetes enviroments (or other e.g coda) [link](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-packages-using-pip-and-virtual-environments)
3. JRE need to be installed - for spark (sudo apt install default-jre)
4. Configure connection with your git repository (GitHub, ADO, etc) via https or [ssh](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) 

## connect to databricks

![Configuration params from url](/image/configuration_from_link.png)

1. Create [venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) and activate it
2. Install databricks connector in corresponding with your cluster version 
```bash
pip install -U "databricks-connect==7.3.*")
```
3. Run 
```bash
databricks-connect configure
```
Provide all prompted info. All info you can find in cluster url (above) and how to get personal token you can find [here](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/authentication#--generate-a-personal-access-token)  
Default port number is 15001.
4. Test your connection
```bash
databricks-connect test
```

## Clone repo and connecto to IDE (VSC)

1. Create dir for new repo
```bash
mkdir ~/path/to/repo/
```
2. Clone git (github or other) repository
```bash
git clone git@github.com:michalmi-dss/databricks_connector_demo.git .
```
3. Open folder with repo in IDE
VSC will automaticly connect with git repo
![git in vsc](/image/git.png)

## Connect your IDE to Databricks (python venv)

To connect IDE to databricks cluster you simply need to connect your IDE to created venv with databricks connector  
How to do that in VSC:
1. Clik F1 and start writing "Python: Select Interpreter"
![select interpreter](/image/select_interpreter.png)
2. Point to python executable file in created venv
![selected interpreter](/image/python37_venv_interpreter.png)
3. Ready you are connected!
4. Run ./test.py code