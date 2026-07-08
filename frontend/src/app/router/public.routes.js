import MainLayout from "@/app/layouts/MainLayout.vue";

import AuthLayout from "@/app/layouts/AuthLayout.vue";

import CheckoutLayout from "@/app/layouts/CheckoutLayout.vue";

export const publicRoutes = [
  {
    path: "/",
    component: MainLayout,

    children: [
      {
        path: "",
        name: "home",
        component: () =>
          import(
            "@/modules/home/views/HomeView.vue"
          ),
      },

      {
        path: "products",
        name: "products",
        component: () =>
          import(
            "@/modules/products/views/ProductsView.vue"
          ),
      },

      {
        path: "products/:slug",
        name: "product-detail",
        component: () =>
          import(
            "@/modules/products/views/ProductDetailView.vue"
          ),
      },

      {
        path: "cart",
        name: "cart",
        component: () =>
          import(
            "@/modules/cart/views/CartView.vue"
          ),
      },

      {
        path: "wishlist",
        name: "wishlist",
        component: () =>
          import(
            "@/modules/wishlist/views/WishlistView.vue"
          ),
      },

      {
        path: "account",
        name: "account",
        component: () =>
          import(
            "@/modules/account/views/AccountView.vue"
          ),
        meta: {
          requiresAuth: true,
        },
      },

      {
        path: "account/orders",
        name: "orders",
        component: () =>
          import(
            "@/modules/account/views/OrdersView.vue"
          ),
        meta: {
          requiresAuth: true,
        },
      },

      {
        path: "account/orders/:orderNumber",
        name: "order-detail",
        component: () =>
          import(
            "@/modules/account/views/OrderDetailView.vue"
          ),
        meta: {
          requiresAuth: true,
        },
      },

      {
        path: "account/addresses",
        name: "addresses",
        component: () =>
          import(
            "@/modules/account/views/AddressesView.vue"
          ),
        meta: {
          requiresAuth: true,
        },
      },

      {
        path: "account/profile",
        name: "profile",
        component: () =>
          import(
            "@/modules/account/views/ProfileView.vue"
          ),
        meta: {
          requiresAuth: true,
        },
      },

      {
        path: "account/security",
        name: "security",
        component: () =>
          import(
            "@/modules/account/views/SecurityView.vue"
          ),
        meta: {
          requiresAuth: true,
        },
      },
    ],
  },

  {
    path: "/",
    component: AuthLayout,

    children: [
      {
        path: "login",
        name: "login",
        component: () =>
          import(
            "@/modules/auth/views/LoginView.vue"
          ),
      },

      {
        path: "register",
        name: "register",
        component: () =>
          import(
            "@/modules/auth/views/RegisterView.vue"
          ),
      },
    ],
  },

  {
    path: "/",
    component: CheckoutLayout,

    children: [
      {
        path: "checkout",
        name: "checkout",
        component: () =>
          import(
            "@/modules/checkout/views/CheckoutView.vue"
          ),
      },
    ],
  },
];
