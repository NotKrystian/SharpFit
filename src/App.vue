<template>
  <div class="app">
    <header>
      <h1>SharpFit</h1>
      <nav>
       <router-link to="/">Home</router-link>
       <router-link to="/results">Results</router-link>
      </nav>
    </header>

    <router-view />
 
    <footer>
      <p>&copy; 2025 SharpFit Clothing Store</p>
    </footer>
  </div>
</template>

<script>

</script>

<style scoped>
.app {
  background-color: #f9f9f9;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

header {
  background-color: #222;
  color: #fff;
  padding: 1rem;
  text-align: center;
}

nav {
  margin-top: 0.5rem;
}

nav a {
  color: #fff;
  margin: 0 0.75rem;
  text-decoration: none;
}

nav a:hover {
  text-decoration: underline;
}

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

footer {
  margin-top: auto;
  background-color: #222;
  color: #fff;
  text-align: center;
  padding: 1rem;
}
</style>
