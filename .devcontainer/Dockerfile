FROM python:3.11-slim-bullseye

RUN pip install --upgrade pip \
 && pip install ipython \
                pytest \
                ruff \
                pydantic

CMD ["ipython"]