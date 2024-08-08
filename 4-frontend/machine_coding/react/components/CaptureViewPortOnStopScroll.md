We have to capture the product's visible on the view port if the user stop scrolling.


Approach 1:

SDK

```css
.wrapper {
  display: flex;
  alight-items: center;
  justify-content: center;
  flex-wrap: wrap;
}

.blocks {
  
}
```

```html
<div class="wrapper">
  <div class="blocks">1</div>
  <div class="blocks">2</div>
  <div class="blocks">3</div>
  <div class="blocks">4</div>
  <div class="blocks">5</div> 
  <div class="blocks">6</div>
</div>
```

```js
// if user stops scroll (debounce scroll event)
// detect html elements in viewport

const inViewPort = (elm) => {
   const elmDim = elm.getBoundingClientRect();
   const viewHeight = window.innerHeight || document.documentElement.clientHeight;
   const viewWidth = window.innerWidth || document.documentElement.clientWidth;

   return elmDim.top >= 0 && elmDim.left >= 0 && elmDim.right < viewWidth && elem.bottom <=viewHeight;
} 

const detect = () => {
   const result = [];
   
   const blocks = document.getSelectorAll(".blocks");
   blocks.forEach((elm)=> {
     if(inViewPort(elm))
     result.push(elm.textContent);
   })
}

const debounce = (func, delay) => {
    let inDebounce;

    return function() {
       const context = this;
       const args = arguments;
  
       clearTimeout(inDebounce);
       inDebounce = setTimout(()=> func.apply(context, args), delay)
    }
}

const debounceDetect = debounce(detect, 1000)

window.addEventListener('scroll', debounceDetect, false)



```
