#   |                                                          |
# --+----------------------------------------------------------+--
#   |   Code by : yasserbdj96                                  |
#   |   Email   : yasser.bdj96@gmail.com                       |
#   |   Github  : https://github.com/yasserbdj96               |
#   |   BTC     : bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9   |
# --+----------------------------------------------------------+--  
#   |        all posts #yasserbdj96 ,all views my own.         |
# --+----------------------------------------------------------+--
#   |                                                          |

#START{
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

RUN = run.py --headless $(headless) --json_data $(json_data) --opiration_title $(opiration_title) --argvs $(argvs) --exec_path $(exec_path)

# make run headless=<True/False> json_data='<PATH_TO_YOUR_JSON_FILE>*' opiration_title='<TITLE_OF_OPIRATION>*' argvs='{"<ARGV_DATA_ID>":"<DATA_TO_INPUT>"}' exec_path='<CHROMEDRIVER_PATH>'
# EX:
# make run headless=False json_data="./imbot-examples/google.json" opiration_title="search" argvs='{"search_for":"yasserbdj96 github"}' exec_path="./chromedriver"
# *    = All inputs must be entered.

run: $(VENV)/bin/activate
	$(PYTHON) $(RUN)

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r ./requirements.txt

clean:
	rm -rf ashar/__pycache__
	rm -rf $(VENV)
#}END.