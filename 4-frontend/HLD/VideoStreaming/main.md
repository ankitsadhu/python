# Video Steaming Websites

Popular Websites

- HULU
- Netflix
- Amazon Prime Video
- Disney + hostar
- Youtube

Services:

- Pre recorder video streaming on demand
- Live Streaming services (news, sports, gaming stream (twitch), personal vlogs(youtube))

## Requirements

Here we are only looking for prerecorded video

Platforms - mobile, tablets, desktop

Offline feature

Search Functionality

Multilingual


### Functional Requirements

- Main page (Contains promo movie, popular movies, personal recomendation)
- Video Player
- Search Bar - Search by genres, actors, movies

### Non Functional

Perfomance

A11y

Localization

Video Protection

Offline Mode

Devices - Desktop, mobile, tablet


## UI

![1723144551470](image/main/1723144551470.png)


## High level Architecture

![1723144584830](image/main/1723144584830.png)

Frontend Contain three parts

1. UI - Main Page, Search, Player
2. Controller (User Events, Proxy layer b/w model & view, Data transformation, filteration)
3. API - Handles API Calls, errors, cache

## Render CSR or SSR or Hydration

![1723144738515](image/main/1723144738515.png)

![1723144835708](image/main/1723144835708.png)

![1723144892864](image/main/1723144892864.png)

## REST vs GraphQL

![1723144933041](image/main/1723144933041.png)

![1723144966912](image/main/1723144966912.png)

![1723145026887](image/main/1723145026887.png)

## Data Model

![1723145059996](image/main/1723145059996.png)

![1723145086740](image/main/1723145086740.png)

## How we deliver video to client (Progessive Dowloading or Streaming)


![1723145119272](image/main/1723145119272.png)

![1723145151077](image/main/1723145151077.png)

![1723145165899](image/main/1723145165899.png)

![1723145234976](image/main/1723145234976.png)

## Streaming Protocol (HLS or MPEG DASH)

![1723145262257](image/main/1723145262257.png)

![1723145328648](image/main/1723145328648.png)

![1723145362786](image/main/1723145362786.png)

## Adaptive Bitrate Streaming

![1723145395753](image/main/1723145395753.png)

![1723145412471](image/main/1723145412471.png)

![1723145440666](image/main/1723145440666.png)

## Offline Mode

### How offline mode should look like

![1723145507943](image/main/1723145507943.png)

![1723145532273](image/main/1723145532273.png)

![1723145553204](image/main/1723145553204.png)

![1723145576446](image/main/1723145576446.png)

### Enable offline with Service worker

![1723145607129](image/main/1723145607129.png)

![1723145625570](image/main/1723145625570.png)

![1723145666740](image/main/1723145666740.png)

## I18n

![1723145720265](image/main/1723145720265.png)

## A11y

![1723145798949](image/main/1723145798949.png)

## Security

![1723145854635](image/main/1723145854635.png)
