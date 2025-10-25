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

        <!-- Size selectors -->
        <div class="selectors">
          <select v-model="product.selectedChest">
            <option disabled value="">Chest (in)</option>
            <option v-for="n in chestSizes" :key="n" :value="n">{{ n }}"</option>
          </select>

          <select v-model="product.selectedSize">
            <option disabled value="">Size</option>
            <option v-for="size in sizes" :key="size" :value="size">{{ size }}</option>
          </select>
        </div>

        <button @click="addToCart(product)">
          Add to Cart
        </button>
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
      chestSizes: Array.from({ length: 23 }, (_, i) => 34 + i), // 34-56
      sizes: ['S', 'M', 'L', 'XL', 'XXL'],
      products: [
        { id: 1, name: 'Classic Tuxedo', price: '$499.99', image: 'https://via.placeholder.com/300x400?text=Classic+Tuxedo', selectedChest: '', selectedSize: '' },
        { id: 2, name: 'Slim Fit Suit', price: '$399.99', image: 'https://via.placeholder.com/300x400?text=Slim+Fit+Suit', selectedChest: '', selectedSize: '' },
        { id: 3, name: 'Modern Blazer', price: '$349.99', image: 'https://via.placeholder.com/300x400?text=Modern+Blazer', selectedChest: '', selectedSize: '' },
        { id: 4, name: 'Luxury Hoodie Suit', price: '$299.99', image: 'https://via.placeholder.com/300x400?text=Luxury+Hoodie+Suit', selectedChest: '', selectedSize: '' }
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
      if (!product.selectedChest || !product.selectedSize) {
        alert('Please select chest size and overall size.')
        return
      }
      alert(`Added to cart: ${product.name} - Chest: ${product.selectedChest}", Size: ${product.selectedSize}`)
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
  text-align: center;
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

/* Selectors */
.selectors {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.selectors select {
  flex: 1;
  padding: 0.6rem 1rem;
  border-radius: 50px;
  border: 1px solid #ccc;
  font-size: 0.95rem;
  outline: none;
  text-align: center;
  appearance: none; /* remove default arrow */
  background-color: #f8f8f8;
  transition: all 0.3s ease;
  cursor: pointer;
}

.selectors select:focus {
  border-color: #aaa;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.selectors select:hover {
  background-color: #f0f0f0;
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
