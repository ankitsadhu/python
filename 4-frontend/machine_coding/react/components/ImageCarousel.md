# Carousel

```js
import "./styles.css";
import { useState } from "react";

export default function App() {
  const images = [
    {
      image_url:
        "https://img.freepik.com/free-photo/young-female-jacket-shorts-presenting-comparing-something-looking-confident-front-view_176474-37521.jpg?w=1800&t=st=1693037944~exp=1693038544~hmac=97e967909706f9b73b4b47d521acf54806f4b9b3efab6196bc8a69f07efff554",
      caption: "Image 1"
    },
    {
      image_url:
        "https://img.freepik.com/free-photo/girl-grey-shirt-showing-something-her-hand_144627-51099.jpg?t=st=1693037931~exp=1693038531~hmac=63713e5a5cf2d23f53ca82b9996ad224ac6e92d0275a53b6debbe6523d7df020",
      caption: "Image 2"
    },
    {
      image_url:
        "https://img.freepik.com/free-photo/young-lady-shirt-jacket-making-scales-gesture-looking-cheerful-front-view_176474-85195.jpg?t=st=1693037931~exp=1693038531~hmac=2f83b6689538e4056912c96f448163e9ef10998f48f671b7e50279f81611fbe6",
      caption: "Image 3"
    },
    {
      image_url:
        "https://img.freepik.com/free-photo/girl-wide-opening-hands-giving-explanation-high-quality-photo_144627-60466.jpg?w=1800&t=st=1693038021~exp=1693038621~hmac=d4520cd86b2aea3e5dda765ede05bb53d70e18a574756d0f41a6806fe325d26d",
      caption: "Image 4"
    }
  ];

  return (
    <div className="App">
      <SlideShow images={images} />
    </div>
  );
}

const SlideShow = ({ images }) => {
  const [active, setActive] = useState(0);

  const onNext = () => {
    if (active < images.length - 1) {
      setActive(active + 1);
    }
  };

  const onPrev = () => {
    if (active > 0) {
      setActive(active - 1);
    }
  };

  return (
    <div className="slideshow">
      {images.map((e, i) => (
        <Slide {...e} key={e.caption} active={i === active} />
      ))}
      <div className="bulleted-navigation">
        {images.map((e, i) => (
          <div
            className={`dot ${i === active ? "active" : ""}`}
            key={e.caption}
            onClick={() => setActive(i)}
          />
        ))}
      </div>
      <div className="next-prev-navigation">
        <div className="navigation next" onClick={onNext}>
          >
        </div>
        <div className="navigation prev" onClick={onPrev}>
          <
        </div>
      </div>
    </div>
  );
};

const Slide = ({ image_url, caption, active }) => {
  return (
    <div className={`slide ${active ? "active" : ""}`}>
      <img src={image_url} alt={caption} />
      <span>{caption}</span>
    </div>
  );
};

```


```css
.App {
  font-family: sans-serif;
  text-align: center;
}

.slideshow {
  position: relative;
  max-width: 500px;
  margin: 20px auto;
}

.slide {
  position: relative;
  display: none;
}

@keyframes fade {
  from {
    opacity: 0.4;
  }
  to {
    opacity: 1;
  }
}

.slide.active {
  display: block;
  animation-name: fade;
  animation-duration: 1.5s;
}

.slide img {
  max-width: 100%;
}

.slide span {
  position: absolute;
  left: 50%;
  bottom: 20px;
  transform: translateX(-50%);
  color: #fff;
}

.bulleted-navigation {
  display: flex;
  align-items: center;
  justify-content: center;
}

.dot {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: grey;
  margin: 0 3px;
  transition: all 0.2s ease;
  cursor: pointer;
}

.dot.active {
  background-color: skyblue;
}

.navigation {
  position: absolute;
  top: 50%;
  transform: translateY(-100%);
  font-size: 2em;
  cursor: pointer;
}

.prev {
  left: 10px;
}

.next {
  right: 10px;
}

```
