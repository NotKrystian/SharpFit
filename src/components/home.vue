<template>
<div class="search-container">
  <input v-model="message" placeholder="Search" />
  <button class="cameraButton" @click="openCamera">Camera</button>
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.search-container {
  display: flex;
  justify-content: center; /* center horizontally */
  align-items: center;
  gap: 0.5rem; /* space between input and button */
  margin: 2rem 0;
  width: 100%;
}

.search-container input,
.search-container .cameraButton {
  flex: 1; /* equal width */
  max-width: 300px; /* optional: limit maximum size */
  padding: 0.5rem;
  border-radius: 4px;
  border: 1px solid #ccc;
  text-align: center; /* center placeholder text */
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

h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
