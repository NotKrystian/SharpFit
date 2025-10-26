<template>
  <div class="home-page">
    <header>
      <p class="tagline">Enter your occasion below and attach a photo of yourself with 30cm between your heels and your hands on the sides of your chest facing forward towards the camera to analyse your body and suggest suits that are in stock and that fit your occasion.</p>
    </header>

    <div class="search-container">
      <input v-model="message" placeholder="Describe your occasion..." />
      <button class="cameraButton" @click="openCamera">Camera</button>
      <input
        ref="fileInput"
        type="file"
        accept="image/*"
        capture="environment"
        @change="onFileSelect"
        style="display:none"
      />
      <button class="submitButton" :disabled="!file || loading" @click="submitForm">
        {{ loading ? "Processing..." : "Submit" }}
      </button>
    </div>

    <p v-if="fileName" class="file-status">✅ {{ fileName }} selected</p>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      message: '',
      file: null,
      fileName: '',
      loading: false
    }
  },
  methods: {
    openCamera() {
      this.$refs.fileInput.click()
    },
    onFileSelect(e) {
      const selectedFile = e.target.files?.[0]
      if (!selectedFile) return
      this.file = selectedFile
      this.fileName = selectedFile.name
    },
    async submitForm() {
      if (!this.file) {
        alert('Please select an image first.')
        return
      }

      this.loading = true
      const formData = new FormData()
      formData.append('sentence', this.message)
      formData.append('image', this.file)

      try {
        const res = await fetch('http://localhost:8000/process', {
          method: 'POST',
          body: formData
        })

        if (!res.ok) {
          throw new Error(`Server responded with ${res.status}`)
        }

        const data = await res.json()

        if (data.redirect) {
          window.location.href = data.redirect
        } else {
          alert('Unexpected response from server.')
          console.log('Response:', data)
        }
      } catch (err) {
        console.error('Upload failed:', err)
        alert('Failed to send image. Check console for details.')
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.home-page {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  color: #222;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 3rem 1rem;
}

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
  color: #b82d77;
  letter-spacing: 0.5px;
}

.search-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
  width: 100%;
  max-width: 700px;
  flex-wrap: wrap;
}

.search-container input,
.search-container .cameraButton,
.search-container .submitButton {
  flex: 1;
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

.cameraButton,
.submitButton {
  background-color: #111;
  color: #fff;
  border: none;
  font-weight: 600;
  letter-spacing: 0.5px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.cameraButton:hover,
.submitButton:hover {
  background-color: #444;
}

.submitButton:disabled {
  background-color: #777;
  cursor: not-allowed;
}

.file-status {
  margin-top: 1rem;
  color: #28a745;
  font-weight: 500;
}
</style>
