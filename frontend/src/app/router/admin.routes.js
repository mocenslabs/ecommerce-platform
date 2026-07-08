import AdminLayout from '@/app/layouts/AdminLayout.vue'

import AdminCustomersView from '@/modules/admin/views/AdminCustomersView.vue'
import AdminPaymentsView from '@/modules/admin/views/AdminPaymentsView.vue'

export const adminRoutes = [
  {
    path: '/admin',

    component: AdminLayout,

    meta: {
      requiresAuth: true,
      requiresAdmin: true,
    },

    children: [
      {
        path: '',
        name: 'admin-dashboard',
        component: () =>
          import(
            '@/modules/admin/views/AdminDashboardView.vue'
          ),
      },

      {
        path: 'products',
        name: 'admin-products',
        component: () =>
          import(
            '@/modules/admin/views/AdminProductsView.vue'
          ),
      },

      {
        path: 'categories',
        name: 'admin-categories',
        component: () =>
          import(
            '@/modules/admin/views/AdminCategoriesView.vue'
          ),
      },

      {
        path: 'brands',
        name: 'admin-brands',
        component: () =>
          import(
            '@/modules/admin/views/AdminBrandsView.vue'
          ),
      },

      {
        path: 'product-images',
        name: 'admin-product-images',
        component: () =>
          import(
            '@/modules/admin/views/AdminProductImagesView.vue'
          ),
      },

      {
        path: 'inventory',
        name: 'admin-inventory',
        component: () =>
          import(
            '@/modules/admin/views/AdminInventoryView.vue'
          ),
      },

      {
        path: 'orders',
        name: 'admin-orders',
        component: () =>
          import(
            '@/modules/admin/views/AdminOrdersView.vue'
          ),
      },

      {
        path: 'orders/:id',
        name: 'admin-order-detail',
        component: () =>
          import(
            '@/modules/admin/views/AdminOrderDetailView.vue'
          ),
      },

      {
        path: 'payments',
        name: 'admin-payments',
        component: AdminPaymentsView,
      },

      {
        path: 'reviews',
        name: 'admin-reviews',
        component: () =>
          import(
            '@/modules/admin/views/AdminReviewsView.vue'
          ),
      },

      {
        path: 'customers',
        name: 'admin-customers',
        component: AdminCustomersView,
      },

      {
        path: 'shipping-methods',
        name: 'admin-shipping-methods',
        component: () =>
          import(
            '@/modules/admin/views/AdminShippingMethodsView.vue'
          ),
      },

      {
        path: 'discounts',
        name: 'admin-discounts',
        component: () =>
          import(
            '@/modules/admin/views/AdminDiscountsView.vue'
          ),
      },
    ],
  },
]
