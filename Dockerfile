FROM python:3
COPY parse.py ~/
RUN pip install requests beautifulSoup4 lxml tabulate
CMD ["python", "~/parse.py"]