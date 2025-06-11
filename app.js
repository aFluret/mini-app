let cart = [];

async function fetchProducts() {
    const res = await fetch('products.json');
    return await res.json();
}

function renderProducts(products) {
    const container = document.getElementById('products');
    products.forEach(p => {
        const div = document.createElement('div');
        div.innerHTML = `
            <strong>${p.name}</strong> (${p.volume}) — ${p.price} ₽<br/>
            <img src=${p.image}>
            <button onclick="addToCart(${p.id}, '${p.name}', ${p.price})">Добавить</button>
        `;
        container.appendChild(div);
    });
}

function addToCart(id, name, price) {
    cart.push({ id, name, price });
    updateCart();
    alert("Добавлено в корзину");
}

function updateCart() {
    const ul = document.getElementById('cart');
    ul.innerHTML = '';
    cart.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name} — ${item.price} ₽`;
        ul.appendChild(li);
    });
}

function sendOrder() {
    if (!cart.length) return alert("Корзина пуста");

    const orderData = {
        total: cart.reduce((sum, item) => sum + item.price, 0),
        items: cart,
        user: Telegram.WebApp.initDataUnsafe.user
    };

    Telegram.WebApp.sendData(JSON.stringify(orderData));
    alert("Заказ отправлен!");
}

// Запуск
fetchProducts().then(renderProducts);