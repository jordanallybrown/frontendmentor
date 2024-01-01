# Frontend Mentor - Blog preview card solution

This is my solution to the [Blog preview card challenge on Frontend Mentor](https://www.frontendmentor.io/challenges/blog-preview-card-ckPaj01IcS).

## What I learned

To create the img zoom on hover state, I achieved this by using a combination of object-fit, transition, and scaling (source from StackOverflow link below). I also had to define a container class around the img to make this work (placing the class directly on the img doesn't):

```html
<div class="card__feature">
  <img
    src="./assets/images/illustration-article.svg"
    alt="Article illustration for blog post"
  />
</div>
```

```css
.card__feature {
  /* max-width: 100%; or exact px size 300px? Not sure if this is needed */
  overflow: hidden; /* ensures img does not stretch outside of its size bounds */
  border-radius: 10px;
}

.card__feature img {
  width: 100%;
  object-fit: cover;
  transition: all 0.3s ease;
}

.card__feature img:hover {
  transform: scale(1.2);
}
```

How to get the font size to change sizes according to the viewport size without a media query:

```css
--fs-lg: clamp(1.25rem, 1.162rem + 0.3756vw, 1.5rem);
```

- [Calculator for Clamp args to change font size based on viewport](https://css-tricks.com/linearly-scale-font-size-with-css-clamp-based-on-the-viewport/#for-those-who-dont-mind-that-edge-case)
- [Medium article explanation for clamp](https://blog.bitsrc.io/css-clamp-the-responsive-combination-weve-all-been-waiting-for-f1ce1981ea6e)

## Useful Resources

- [StackOverflow Img Zoom Affect](https://stackoverflow.com/questions/69491728/how-to-zoom-an-image-on-mouse-hover-using-css)
- [W3C Smooth Transition Hover text](https://www.w3schools.com/howto/howto_css_transition_hover.asp)
- [Cool card move effect when hovering via Figma example](https://help.figma.com/hc/en-us/articles/360039956894-Add-a-font-to-Figma-design)
