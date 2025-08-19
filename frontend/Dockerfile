FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN pip install streamlit requests pandas streamlit-autorefresh plotly

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
