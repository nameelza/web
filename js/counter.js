let counter = 0;

function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('button').onclick = () => {
        setInterval(count, 1000);
    }
});