FROM python:3.13-slim-bookworm

RUN pip install --upgrade pip \
 && pip install ipython \
                pytest \
                ruff \
                pydantic

CMD ["ipython"]