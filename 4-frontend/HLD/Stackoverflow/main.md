1. Quora
2. reddit
3. stackoverflow

## Features

- Feeds
- Post Creation
- Post Search
- Likes
- Subscribe to intersting post & notify
- Text Editor - support code block & images
- Latest post or most popular post

### Functional Requirement

What web app must do

- Feed
- Search
- Creating Post
- Comments
- Votes (Likes)

### Non Functional

How the app should work

- Real Time updates
- Adaption on all devices
- Performance
- A11y
- Security
- i18n

## Architecture

Real time updates - websocket

Static Files - CDN

Relational DB - as data are coupled together


## CSR os SSR

![1723146462432](image/main/1723146462432.png)

![1723146535783](image/main/1723146535783.png)

## Data Model

![1723146591806](image/main/1723146591806.png)

## Pagination

![1723146644514](image/main/1723146644514.png)

![1723146670932](image/main/1723146670932.png)

![1723146707988](image/main/1723146707988.png)

## API Endpoints

![1723146752006](image/main/1723146752006.png)

Case1: Convert K incase of too many votes

Case2: What if user tries to vote from two devices?

### API Versioning

![1723146867126](image/main/1723146867126.png)

### Text Editor

1. HTML Elemets Support
   1. contentEditable & execCommand
2. Markdown
   1. CommonMark (standardized version of markdown) ✅
3. Latex
