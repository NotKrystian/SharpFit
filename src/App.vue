<template>
  <div class="app">
    <header>
      <h1>SharpFit</h1>
      <p class="tagline">Luxury Suits for the Modern Gentleman</p>
      <nav>
        <router-link to="/">Home</router-link>
        <router-link to="/results">Shop</router-link>
      </nav>
    </header>

    <main>
      <router-view />
    </main>

    <footer>
      <p>&copy; 2025 SharpFit Clothing Store</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style scoped>
.app {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  background-color: #fdfdfd;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Header */
header {
  background-color: #111;
  color: #fff;
  text-align: center;
  padding: 2rem 1rem;
}

header h1 {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

header .tagline {
  font-size: 1.2rem;
  font-weight: 400;
  color: #aaa;
  margin-bottom: 1rem;
  letter-spacing: 0.5px;
}

/* Navigation */
nav a {
  color: #fff;
  margin: 0 1rem;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease;
}

nav a:hover {
  color: #42b983;
}

/* Main */
main {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem 1rem;
}

/* Footer */
footer {
  background-color: #111;
  color: #aaa;
  text-align: center;
  padding: 1rem;
  font-size: 0.9rem;
}
</style>
