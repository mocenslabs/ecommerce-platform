<script setup>
import Navbar from '@/components/navigation/Navbar.vue'
import Footer from '@/components/navigation/Footer.vue'
</script>

<template>
  <div
    class="min-h-screen flex flex-col bg-white text-slate-900 dark:bg-slate-950 dark:text-white transition-colors"
  >
    <Navbar />

    <main class="flex-1">
      <router-view />
    </main>

    <Footer />
  </div>
</template>
