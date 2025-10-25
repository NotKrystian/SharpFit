<template>
  <div class="home-page">
    <header>
      <h1>SharpFit</h1>
      <p class="tagline">Luxury Suits for the Modern Gentleman</p>
    </header>

    <div class="search-container">
      <input v-model="message" placeholder="Search for premium suits..." />
      <button class="cameraButton" @click="openCamera">Camera</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      message: ''
    }
  },
  methods: {
    openCamera () {
      alert('Camera button clicked!')
    }
  }
}
</script>

<style scoped>
/* Page layout */
.home-page {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  color: #222;
  background-color: #fdfdfd;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 3rem 1rem;
}

/* Header */
header {
  text-align: center;
  margin-bottom: 3rem;
}

header h1 {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: #111;
}

header .tagline {
  font-size: 1.2rem;
  color: #555;
  letter-spacing: 0.5px;
}

/* Search bar */
.search-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
  width: 100%;
  max-width: 600px;
}

.search-container input,
.search-container .cameraButton {
  flex: 1; /* equal width */
  padding: 0.75rem 1rem;
  border-radius: 50px;
  border: 1px solid #ccc;
  font-size: 1rem;
  outline: none;
  text-align: center;
  transition: box-shadow 0.3s ease;
}

.search-container input:focus {
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
  border-color: #aaa;
}

.search-container .cameraButton {
  background-color: #111;
  color: #fff;
  border: none;
  font-weight: 600;
  letter-spacing: 0.5px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.search-container .cameraButton:hover {
  background-color: #444;
}

/* Typography resets */
h1, h2 {
  font-weight: 600;
  margin: 0;
}

p {
  margin: 0;
}
</style>
