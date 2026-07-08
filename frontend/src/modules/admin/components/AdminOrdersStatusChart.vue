<script setup>
import {
  computed,
} from 'vue'

import {
  Doughnut,
} from 'vue-chartjs'

import {
  Chart,
  ArcElement,
  Tooltip,
  Legend,
} from 'chart.js'

Chart.register(
  ArcElement,
  Tooltip,
  Legend
)

const props = defineProps({
  data: {
    type: Array,
    default: () => [],
  },
})

const chartData =
  computed(() => ({
    labels:
      props.data.map(
        item =>
          item.status
      ),

    datasets: [
      {
        data:
          props.data.map(
            item =>
              item.total
          ),
      },
    ],
  }))
</script>

<template>
  <div class="h-80">
    <Doughnut
      :data="chartData"
    />
  </div>
</template>
