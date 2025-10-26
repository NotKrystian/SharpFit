<template>
  <div class="results-page">
    <header>
      <h1>SharpFit Results</h1>
      <p class="sub">Recommended suits for chest {{ chest }}</p>
    </header>

    <div v-if="ids.length" class="grid">
      <div v-for="id in ids" :key="id" class="card">
        <img
          :src="getImagePath(id)"
          :alt="`Suit ${id}`"
        />
        <div class="meta">
          <h3>Suit {{ id }} — Chest {{ chest }}</h3>
          <p>ID: {{ id }}</p>
        </div>
      </div>
    </div>

    <p v-else class="empty">No suits to show. Go back and try again.</p>

    <div class="actions">
      <button @click="$router.push({ name: 'home' })">Back</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Results',
  data() {
    const q = this.$route.query || {}
    const chest = q.chest ? String(q.chest) : ''
    const ids = (q.ids || '')
      .split(',')
      .filter(Boolean)
    return { chest, ids }
  },
  methods: {
    getImagePath(id) {
      return `/Pictures/${id}.jpg`
    }
  }
}
</script>

<style scoped>
.results-page {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  color: #222;
  padding: 2rem 1rem 3rem;
  max-width: 1100px;
  margin: 0 auto;
}
header {
  text-align: center;
  margin-bottom: 2rem;
}
.sub {
  color: #666;
  margin-top: .25rem;
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px,1fr));
  gap: 1rem;
}
.card {
  background: #fff;
  border: 1px solid #e8e8e8;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 4px 14px rgba(0,0,0,.04);
}
.card img {
  width: 100%;
  height: 260px;
  object-fit: cover;
  display: block;
  background: #f5f5f5;
}
.meta {
  padding: .75rem 1rem 1rem;
}
.meta h3 {
  font-size: 1rem;
  margin: 0 0 .25rem;
  font-weight: 700;
}
.meta p {
  margin: 0;
  color: #666;
  font-size: .9rem;
}
.empty {
  text-align: center;
  color: #666;
  margin: 2rem 0;
}
.actions {
  display: flex;
  justify-content: center;
  margin-top: 2rem;
}
.actions button {
  background: #111;
  color: #fff;
  border: none;
  padding: .75rem 1.25rem;
  border-radius: 999px;
  cursor: pointer;
  font-weight: 600;
}
.actions button:hover {
  background: #444;
}
</style>
