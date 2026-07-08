<script setup>
import AdminSidebar from
  '@/modules/admin/components/AdminSidebar.vue'

import AdminNavbar from
  '@/modules/admin/components/AdminNavbar.vue'
</script>

<template>
  <div
    class="flex min-h-screen bg-slate-100 dark:bg-slate-950"
  >
    <AdminSidebar />

    <div
      class="flex min-w-0 flex-1 flex-col"
    >
      <AdminNavbar />

      <main
        class="flex-1 overflow-y-auto p-4 md:p-6"
      >
        <router-view />
      </main>
    </div>
  </div>
</template>
