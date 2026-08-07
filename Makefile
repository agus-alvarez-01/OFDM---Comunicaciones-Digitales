VENV_DIR := venv
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip
REQUIREMENTS := requirements.txt

.PHONY: all venv install kernel activate clean

all: venv install kernel
	@echo ""
	@echo "======================================"
	@echo " Entorno listo."
	@echo "======================================"
	@echo ""
	@echo "Para activarlo ejecutá:"
	@echo "source $(VENV_DIR)/bin/activate"
	@echo ""

venv:
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "==> Creando entorno virtual..."; \
		python3 -m venv $(VENV_DIR); \
	else \
		echo "==> Entorno virtual encontrado."; \
	fi

	@if [ ! -x "$(PYTHON)" ]; then \
		echo "ERROR: La venv no contiene un Python válido."; \
		exit 1; \
	fi

install: venv
	@echo "==> Instalando dependencias..."
	@$(PYTHON) -m pip install --upgrade pip
	@$(PIP) install -r $(REQUIREMENTS)

kernel: install
	@echo "==> Registrando kernel de Jupyter..."
	@$(PYTHON) -m ipykernel install --user \
		--name ofdm \
		--display-name "Python (OFDM)"

activate:
	@echo "Para activar el entorno ejecutá:"
	@echo "source $(VENV_DIR)/bin/activate"

clean:
	@echo "==> Eliminando entorno virtual..."
	@rm -rf $(VENV_DIR)
	@echo "==> Entorno eliminado."