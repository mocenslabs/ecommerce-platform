<script setup>
import { onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { storeToRefs } from 'pinia'

import { useDashboardStore } from '@/stores/dashboard.store'

import AdminStatCard from '@/modules/admin/components/AdminStatsCard.vue'
import AdminCard from '@/modules/admin/components/AdminCard.vue'

import AdminRevenueChart from '@/modules/admin/components/AdminRevenueChart.vue'
import AdminOrdersStatusChart from '@/modules/admin/components/AdminOrdersStatusChart.vue'

const dashboardStore =
  useDashboardStore()

const {
  stats,
  recentOrders,
  topProducts,
  revenueTrend,
  ordersByStatus,
  lowStockProducts,
  loading,
} = storeToRefs(
  dashboardStore
)

onMounted(() => {
  dashboardStore.fetchDashboard()
})
</script>

<template>
  <section>
    <div
      class="mb-8 flex flex-col gap-4 md:flex-row md:items-center md:justify-between"
    >
      <div>
        <h1
          class="text-3xl font-bold text-slate-900 dark:text-white"
        >
          Dashboard
        </h1>

        <p
          class="mt-1 text-sm text-slate-500"
        >
          Overview of your store performance
        </p>
      </div>
    </div>

    <div
      v-if="loading"
      class="py-20 text-center text-slate-500"
    >
      Loading dashboard...
    </div>

    <template v-else>
      <!-- KPIs -->

      <div
        class="grid gap-4 sm:grid-cols-2 xl:grid-cols-4"
      >
        <AdminStatCard
          title="Revenue"
          :value="`$${stats?.total_revenue || 0}`"
        />

        <AdminStatCard
          title="Orders"
          :value="stats?.total_orders || 0"
        />

        <AdminStatCard
          title="Customers"
          :value="stats?.total_customers || 0"
        />

        <AdminStatCard
          title="Products"
          :value="stats?.total_products || 0"
        />
      </div>

      <!-- STATUS -->

      <div
        class="mt-6 grid gap-4 md:grid-cols-3"
      >
        <AdminStatCard
          title="Paid Orders"
          :value="stats?.paid_orders || 0"
        />

        <AdminStatCard
          title="Pending Orders"
          :value="stats?.pending_orders || 0"
        />

        <AdminStatCard
          title="Cancelled Orders"
          :value="stats?.cancelled_orders || 0"
        />
      </div>

      <!-- CHARTS -->

      <div
        class="mt-8 grid gap-6 xl:grid-cols-2"
      >
        <AdminCard
          title="Revenue Trend"
        >
          <AdminRevenueChart
            :data="revenueTrend"
          />
        </AdminCard>

        <AdminCard
          title="Orders By Status"
        >
          <AdminOrdersStatusChart
            :data="ordersByStatus"
          />
        </AdminCard>
      </div>

      <!-- LOW STOCK -->

      <AdminCard
        title="Low Stock Products"
        class="mt-8"
      >
        <div
          v-if="
            !lowStockProducts.length
          "
          class="text-sm text-slate-500"
        >
          No low stock products.
        </div>

        <div
          v-else
          class="overflow-x-auto"
        >
          <table
            class="min-w-full"
          >
            <thead>
              <tr
                class="border-b"
              >
                <th class="p-4 text-left">
                  Product
                </th>

                <th class="p-4 text-left">
                  SKU
                </th>

                <th class="p-4 text-left">
                  Stock
                </th>
              </tr>
            </thead>

            <tbody>
              <tr
                v-for="item in lowStockProducts"
                :key="item.sku"
                class="border-b"
              >
                <td class="p-4">
                  {{ item.product }}
                </td>

                <td class="p-4">
                  {{ item.sku }}
                </td>

                <td
                  class="p-4 font-semibold text-red-500"
                >
                  {{ item.quantity }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </AdminCard>

      <!-- RECENT ORDERS -->

      <AdminCard
        title="Recent Orders"
        class="mt-8"
      >
        <div
          class="overflow-x-auto"
        >
          <table
            class="min-w-full"
          >
            <thead>
              <tr
                class="border-b text-left"
              >
                <th class="p-4">
                  Order
                </th>

                <th class="p-4">
                  Customer
                </th>

                <th class="p-4">
                  Status
                </th>

                <th class="p-4">
                  Total
                </th>
              </tr>
            </thead>

            <tbody>
              <tr
                v-for="order in recentOrders"
                :key="order.id"
                class="border-b"
              >
                <td class="p-4">
                  {{ order.order_number }}
                </td>

                <td class="p-4">
                  {{ order.customer }}
                </td>

                <td class="p-4">
                  {{ order.status }}
                </td>

                <td class="p-4">
                  $
                  {{ order.total_amount }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <template #footer>
          <RouterLink
            to="/admin/orders"
            class="text-sm font-medium text-blue-600 hover:underline"
          >
            View all orders →
          </RouterLink>
        </template>
      </AdminCard>

      <!-- TOP PRODUCTS -->

      <AdminCard
        title="Top Products"
        class="mt-8"
      >
        <div
          class="grid gap-4 md:grid-cols-2"
        >
          <div
            v-for="product in topProducts"
            :key="product.id"
            class="rounded-xl border border-slate-200 p-4 dark:border-slate-700"
          >
            <h3
              class="font-semibold"
            >
              {{ product.name }}
            </h3>

            <p
              class="mt-2 text-sm text-slate-500"
            >
              Sales:
              {{ product.total_sales }}
            </p>

            <p
              class="text-sm text-slate-500"
            >
              Rating:
              {{ product.average_rating }}
            </p>
          </div>
        </div>

        <template #footer>
          <RouterLink
            to="/admin/products"
            class="text-sm font-medium text-blue-600 hover:underline"
          >
            Manage products →
          </RouterLink>
        </template>
      </AdminCard>
    </template>
  </section>
</template>
