<template>
  <div>
    <!-- Search bar -->
    <div class="search-container">
      <input v-model="searchQuery" placeholder="Search products..." />
    </div>

    <!-- Products -->
    <div class="products">
      <div
        class="product-card"
        v-for="product in filteredProducts"
        :key="product.id"
      >
        <img :src="product.image" :alt="product.name" />
        <h2>{{ product.name }}</h2>
        <p class="price">{{ product.price }}</p>
        <button @click="addToCart(product)">Add to Cart</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'results',
  data () {
    return {
      searchQuery: '',
      products: [
        { id: 1, name: 'T-Shirt', price: '$19.99', image: 'https://via.placeholder.com/200x250?text=T-Shirt' },
        { id: 2, name: 'Jeans', price: '$49.99', image: 'https://via.placeholder.com/200x250?text=Jeans' },
        { id: 3, name: 'Hoodie', price: '$39.99', image: 'https://via.placeholder.com/200x250?text=Hoodie' },
        { id: 4, name: 'Sneakers', price: '$59.99', image: 'https://via.placeholder.com/200x250?text=Sneakers' }
      ]
    }
  },
  computed: {
    filteredProducts () {
      if (!this.searchQuery) return this.products
      const query = this.searchQuery.toLowerCase()
      return this.products.filter(p => p.name.toLowerCase().includes(query))
    }
  },
  methods: {
    addToCart (product) {
      alert(`Added to cart: ${product.name}`)
    }
  }
}
</script>

<style scoped>
/* Search bar styles */
.search-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
  margin: 2rem 0;
}

.search-container input,
.search-container .cameraButton {
  flex: 1;
  max-width: 300px;
  padding: 0.5rem;
  border-radius: 4px;
  border: 1px solid #ccc;
  text-align: center;
}

.search-container .cameraButton {
  background-color: #007BFF;
  color: white;
  border: none;
  cursor: pointer;
}

.search-container .cameraButton:hover {
  background-color: #0056b3;
}

/* Product grid */
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
