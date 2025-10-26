<template>
  <div class="app">
    <header>
      <h1>SharpFit</h1>
      <p class="tagline">The future of suit shopping</p>
      <nav>
        <button class="button" style="--clr:#bd1dcc"><router-link to="/">Start Again</router-link></button>
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
  background: #020024;
  background: linear-gradient(nulldeg,rgba(2, 0, 36, 1) 0%, rgba(9, 9, 121, 1) 6%, rgba(0, 212, 255, 1) 100%);
  text-align: center;
  padding: 2rem 1rem;
}

header h1 {
  color:rgb(42, 179, 179);
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

header .tagline {
  font-size: 1.2rem;
  font-weight: 400;
  color:rgb(21, 196, 196);
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
  background: #020024;
  background: linear-gradient(180deg,rgba(2, 0, 36, 1) 0%, rgba(9, 9, 121, 1) 6%, rgba(0, 212, 255, 1) 100%);color: #fff;
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

.button {
  line-height: 1;
  text-decoration: none;
  display: inline-flex;
  border: none;
  cursor: pointer;
  align-items: center;
  gap: 0.75rem;
  background-color: var(--clr);
  color: #fff;
  border-radius: 10rem;
  font-weight: 600;
  padding: 0.75rem 1.5rem;
  padding-left: 20px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  transition: background-color 0.3s;
}

.button__icon-wrapper {
  flex-shrink: 0;
  width: 25px;
  height: 25px;
  position: relative;
  color: var(--clr);
  background-color: #fff;
  border-radius: 50%;
  display: grid;
  place-items: center;
  overflow: hidden;
}

.button:hover {
  background-color: #000;
}

.button:hover .button__icon-wrapper {
  color: #000;
}

.button__icon-svg--copy {
  position: absolute;
  transform: translate(-150%, 150%);
}

.button:hover .button__icon-svg:first-child {
  transition: transform 0.3s ease-in-out;
  transform: translate(150%, -150%);
}

.button:hover .button__icon-svg--copy {
  transition: transform 0.3s ease-in-out 0.1s;
  transform: translate(0);
}

</style>
