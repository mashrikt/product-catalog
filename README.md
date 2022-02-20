# Product Catalog

> a simple system to catalog product images scraped from brand websites

## Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

## Local Development

Start the dev server for local development:

```shell script
$ docker-compose up --build
```

## Features

- Given the product page of a brand website, it will fetch images and some details of that product.
- Returns product images according to size query params of small, medium or large.
- Currently only supports ebay.com pages.
- Currently only fetches the primary image.

## API Structure

- `api/products/`: Products list create. Accepts `size` [small/medium/large] and url query params.
- `api/products/{id}/`: Product retreive API.
- `api/images/`: Images list. Accepts `size` [small/medium/large] query params.
- `api/images/{id}/`: Image retreive API.

## Improvements

- Support more brand websites.
- Fetch more than one image.
- Better error handling
