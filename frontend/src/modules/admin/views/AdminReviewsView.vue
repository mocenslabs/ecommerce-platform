<script setup>
import { onMounted } from 'vue'

import {
  useAdminStore,
} from '@/stores/admin.store'

import AdminPageHeader from
  '@/modules/admin/components/AdminPageHeader.vue'

import AdminTable from
  '@/modules/admin/components/AdminTable.vue'

import AdminEmptyState from
  '@/modules/admin/components/AdminEmptyState.vue'

const adminStore =
  useAdminStore()

const approveReview =
  async (review) => {
    await adminStore.updateReview(
      review.id,
      {
        is_approved:
          !review.is_approved,
      },
    )
  }

const deleteReview =
  async (id) => {
    if (
      !confirm(
        'Delete review?',
      )
    ) {
      return
    }

    await adminStore.deleteReview(
      id,
    )
  }

onMounted(async () => {
  await adminStore.fetchReviews()
})
</script>

<template>
  <section>
    <AdminPageHeader
      title="Reviews"
      subtitle="Manage customer reviews and moderation."
    />

    <AdminEmptyState
      v-if="
        !adminStore.reviews.length
      "
      title="No reviews yet"
      description="Customer reviews will appear here once products receive feedback."
    />

    <AdminTable
      v-else
      :columns="[
        'Product',
        'Customer',
        'Rating',
        'Title',
        'Status',
        'Actions',
      ]"
    >
      <tr
        v-for="review in adminStore.reviews"
        :key="review.id"
        class="border-b border-slate-200 dark:border-slate-800"
      >
        <td
          class="px-4 py-4"
        >
          {{
            review.product_name
          }}
        </td>

        <td
          class="px-4 py-4"
        >
          {{
            review.customer_email
          }}
        </td>

        <td
          class="px-4 py-4"
        >
          ⭐
          {{ review.rating }}
        </td>

        <td
          class="px-4 py-4"
        >
          {{ review.title }}
        </td>

        <td
          class="px-4 py-4"
        >
          <span
            v-if="
              review.is_approved
            "
            class="rounded-full bg-green-100 px-3 py-1 text-xs font-medium text-green-700"
          >
            Approved
          </span>

          <span
            v-else
            class="rounded-full bg-yellow-100 px-3 py-1 text-xs font-medium text-yellow-700"
          >
            Pending
          </span>
        </td>

        <td
          class="px-4 py-4"
        >
          <div
            class="flex gap-2"
          >
            <button
              class="rounded-lg bg-slate-900 px-3 py-2 text-sm font-medium text-white transition hover:opacity-90"
              @click="
                approveReview(
                  review,
                )
              "
            >
              {{
                review.is_approved
                  ? 'Hide'
                  : 'Approve'
              }}
            </button>

            <button
              class="rounded-lg bg-red-600 px-3 py-2 text-sm font-medium text-white transition hover:opacity-90"
              @click="
                deleteReview(
                  review.id,
                )
              "
            >
              Delete
            </button>
          </div>
        </td>
      </tr>
    </AdminTable>
  </section>
</template>
