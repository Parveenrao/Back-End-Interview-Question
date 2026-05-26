"""   
name: Full CI/CD Pipeline

on:
  push:
    branches: [main]

jobs:

  lint:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - run: pip install flake8 black

      - run: flake8 .
      - run: black --check .

  test:
    runs-on: ubuntu-latest
    needs: lint

    strategy:
      matrix:
        python-version: [3.9, 3.10]

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Cache deps
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}

      - run: pip install -r requirements.txt
      - run: pytest

  build:
    runs-on: ubuntu-latest
    needs: test

    steps:
      - uses: actions/checkout@v4

      - name: Build app
        run: |
          mkdir build
          echo "build output" > build/app.txt

      - name: Upload build
        uses: actions/upload-artifact@v4
        with:
          name: build-files
          path: build/

  deploy:
    runs-on: ubuntu-latest
    needs: build

    steps:
      - name: Download build
        uses: actions/download-artifact@v4
        with:
          name: build-files

      - name: Deploy
        run: echo "Deploying app..."

"""

# 1. Lint (Code quality check , fail early is bad)
# 2. Test (Matrix) -> Run test on multiple python env , use cache - faster 
# 3. Build -> Create output , Upload artifact 
# 4. Deploy -> Download artifact 