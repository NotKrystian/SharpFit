<template>
  <div class="results-page">
    <!-- Search bar -->
    <div class="search-container">
      <input v-model="searchQuery" placeholder="Search for premium suits..." />
    </div>

    <!-- Products -->
    <div class="products">
      <div
        class="product-card"
        v-for="product in filteredProducts"
        :key="product.id"
      >
        <div class="image-wrapper">
          <img :src="product.image" :alt="product.name" />
        </div>
        <h2 class="product-name">{{ product.name }}</h2>
        <p class="price">{{ product.price }}</p>
        <button @click="addToCart(product)">Add to Cart</button>
      </div>
      <p v-if="filteredProducts.length === 0" class="no-results">No products found.</p>
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
        { id: 1, name: 'Classic Tuxedo', price: '$499.99', image: 'https://via.placeholder.com/300x400?text=Classic+Tuxedo' },
        { id: 2, name: 'Slim Fit Suit', price: '$399.99', image: 'https://via.placeholder.com/300x400?text=Slim+Fit+Suit' },
        { id: 3, name: 'Modern Blazer', price: '$349.99', image: 'https://via.placeholder.com/300x400?text=Modern+Blazer' },
        { id: 4, name: 'Luxury Hoodie Suit', price: '$299.99', image: 'https://via.placeholder.com/300x400?text=Luxury+Hoodie+Suit' }
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
/* Base page */
.results-page {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  color: #222;
  background-color: #fdfdfd;
  padding: 2rem 1rem;
}

/* Search bar */
.search-container {
  display: flex;
  justify-content: center;
  margin-bottom: 3rem;
}

.search-container input {
  width: 100%;
  max-width: 400px;
  padding: 0.75rem 1rem;
  border: 1px solid #ccc;
  border-radius: 50px;
  font-size: 1rem;
  outline: none;
  transition: box-shadow 0.3s ease;
}

.search-container input:focus {
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
  border-color: #aaa;
}

/* Product grid */
.products {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 2rem;
}

/* Product card */
.product-card {
  background-color: #fff;
  border-radius: 12px;
  overflow: hidden;
  width: 250px;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 25px rgba(0,0,0,0.15);
}

/* Product image */
.image-wrapper {
  overflow: hidden;
  height: 350px;
}

.product-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.product-card:hover img {
  transform: scale(1.05);
}

/* Product details */
.product-name {
  font-size: 1.2rem;
  font-weight: 600;
  margin: 1rem 0 0.25rem 0;
  color: #111;
}

.price {
  font-size: 1rem;
  font-weight: 500;
  color: #777;
  margin-bottom: 1rem;
}

/* Button */
button {
  background-color: #111;
  color: #fff;
  border: none;
  padding: 0.6rem 1.5rem;
  border-radius: 50px;
  font-weight: 600;
  letter-spacing: 0.5px;
  margin-bottom: 1rem;
  transition: background 0.3s ease;
}

button:hover {
  background-color: #444;
}

/* No results */
.no-results {
  text-align: center;
  font-size: 1.1rem;
  color: #999;
  margin-top: 2rem;
}
</style>
