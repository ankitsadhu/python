**Learnersbucket (12)**

1. FeatureFlag (done)
2. SwitchCase Component (done)
3. Infinite Scroll (done)
4. Capture Product that user is focus at (done)
5. Auto Suggestion Searchbox (done)
6. Pagination & Search (done)
7. Responsive Slide show / Carousel (done)
8. Intro.js or (Step by Step website walk thorugh) [done] (Create SDK)
9. Stepper Component
10. Todo List in React
11. Modal
12. Detect overlapping circle
13. Analytics SDK: https://youtu.be/0T3Qwtot9D0?si=CEp3cl5-HrstCMJw
14. Web Components in React
    1. Virtual Scolling
    2. Countdown timmer
    3. Two Step login form like GMAIL
    4. Employee status toggler

How to build SDK:

https://youtu.be/vRmLTZyq57U?si=exRa_TX2fYSyi1-r

https://youtu.be/sZQEa13r22I?si=GhS1Mll_h8Khsqya

Zoho CRM Widget:

https://www.youtube.com/watch?v=RKGPlEHYiqw

https://www.youtube.com/watch?v=RKGPlEHYiqw

https://youtu.be/v0xI3BaZJWc?si=5k1-HhY-k6HUrN1R

**DevTech Tools**

1. Autocomplete
2. Custom timmer
3. Implement your own DOM
4. Compound Components
5. React window implementation
6. Trello Board
7. Lazy Loading of images
8. Reduce code duplication
9. Build your own Redux

JS

1. Loadash GroupBy
2. Flat version of deeply nested array
3. setTimeout & Interval Polyfill, clear timeout
4. Local Storage API of your own

**Roadside coader**

1. File Explorer
2. pagination
3. Progressbar
4. useMemohook Polyfill
5. useEffect polyfill
6. dark / light mode
7. OTP
8. Stepper
9. useThrottle hook
10. Drag & Drop Notes
11. Tic Tac TOe
12. Toast Component
13. Auto Suggestion
14. Nested Comments
15. like button
16. Grids light

**Atlassian Interview Round (No DSA in Atlassian)**

1. Browser Coding Round(Component Building) [LLD]
   1. Star Rating
2. Vanilla JS (utils, SDK) [Exception Handling, Performance, Design Patterns]
   1. What is a promise?
   2. What are different states of a promise?
   3. How do you create a promise?
   4. How do you resolve it?
   5. Benifits of using Promise?
   6. Challenges of using promise?

      Problem Statement:

      You are a JS dev working on a new weather app.

      You need to make an async request to the OPenWeatherMap API to get the weather data fo r given city.

      1. Step 1: API Calling
      2. Step 2: Concurrency / race condition handling
         1. https://youtu.be/_4Kjw_VVPHA?si=ZGi6X3ocv9-BvSFM
         2. https://youtu.be/d0UT6NtpO4o?si=Ey6QQYi9A9f9PoPE
         3. https://youtu.be/DWZj56qUNfs?si=ysvDd7XlDI4SIwpA
         4. https://youtu.be/9LFNX5p0W-4?si=v_phEuhCn0848f-o
         5. https://youtu.be/xD-aSyqpjWY?si=15trtx3FhceAf0AE
         6. https://youtu.be/wOtEz6MM2zE?si=a1oMqoL0RlwfBHEX
      3. Error Handling
      4. Maybe DOM Traversal, or folder structure
3. System Design Round
   1. Get Comfortable with excallidraw etc
4. Managerial Round (Cultural Fit)

Interview Questions

```js
console.log("A")

setTimeout(()=> {console.log('B)})

['C', 'D'].forEach(x => console.log(x))

console.log('E')

//Output
A
C, D
E
B
```

Q2. Practise reduce method more

Q3. Memoized function

Q4. Flatten an Array

Q5. Create a fetchWithAutoRetry(fetch, cout) which automatically fetch again with error happen untill the max count is met. (also use requestAnimationFrame)

Q6. LRU - Chrome Storage automatic eviction

Optimisation - PriorityQueue or heap

```js
const CACHE_KEYS_SIZE = 20
const cache = {
  
}

function setCache({key, value}) {
   cache[key] ={
	value, 
        time: Date.now()
   }

   const cacheKeys = Object.keys(cache);
   if(cacheKeys > 20) {
     let LRUKEY = cacheKeys[0]
     for(let i=0; i<cacheKeys.length; i++) {
        if(cache[LRUKey]).time > cache[cacheKeys[i].time) {	}
     }
   }

   return {
	setCache,
	getCacheValue
   }

}
```

Vasanth Bhat

**Shivam Bhalla**


1. DSA (linked list, Tree, Hasmap, Recursion, Memoization)
2. JS, HTML, CSS
3. JS Utility Function
4. Games
5. Polyfills
6. Memory Store in JS
7. Machine Coding(LLD)
8. HLD
   1. FB news feed
   2. Ecomerce
