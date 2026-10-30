let cartCount = 0;

function addToCart() {
    cartCount++;
    const counterElement = document.getElementById('cart-counter');
    if (counterElement) {
        counterElement.textContent = cartCount;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    console.log("Script cargado correctamente.");
});