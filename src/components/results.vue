<template>
  <div class="products">
    <div class="product-card" v-for="product in products" :key="product.id">
      <img :src="product.image" :alt="product.name" />
      <h2>{{ product.name }}</h2>
      <p class="price">{{ product.price }}</p>
      <button @click="addToCart(product)">Add to Cart</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'results',
  data() {
    return {
      products: [
        {
          id: 1,
          name: 'T-Shirt',
          price: '$19.99',
          image: 'https://via.placeholder.com/200x250?text=T-Shirt'
        },
        {
          id: 2,
          name: 'Jeans',
          price: '$49.99',
          image: 'https://via.placeholder.com/200x250?text=Jeans'
        },
        {
          id: 3,
          name: 'Hoodie',
          price: '$39.99',
          image: 'https://via.placeholder.com/200x250?text=Hoodie'
        },
        {
          id: 4,
          name: 'Sneakers',
          price: '$59.99',
          image: 'https://via.placeholder.com/200x250?text=Sneakers'
        }
      ]
    }
  },
  methods: {
    addToCart(product) {
      console.log(`Added to cart: ${product.name}`)
      alert(`Added to cart: ${product.name}`)
    }
  }
}
</script>

<style scoped>
.products {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin: 2rem;
}

.product-card {
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin: 1rem;
  padding: 1rem;
  width: 200px;
  text-align: center;
  transition: box-shadow 0.2s;
}

.product-card:hover {
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.product-card img {
  width: 100%;
  border-radius: 4px;
}

.price {
  font-weight: bold;
  color: #333;
}

button {
  margin-top: 0.5rem;
  background-color: #007BFF;
  border: none;
  color: white;
  padding: 0.5rem;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
