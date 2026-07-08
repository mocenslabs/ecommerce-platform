<script setup>
import {
  computed,
} from 'vue'

import {
  Line,
} from 'vue-chartjs'

import {
  Chart,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend,
} from 'chart.js'

Chart.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
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
    labels: props.data.map(
      item =>
        new Date(
          item.month
        ).toLocaleDateString()
    ),

    datasets: [
      {
        label: 'Revenue',

        data: props.data.map(
          item =>
            Number(
              item.revenue
            )
        ),
      },
    ],
  }))

const chartOptions = {
  responsive: true,

  maintainAspectRatio:
    false,
}
</script>

<template>
  <div class="h-80">
    <Line
      :data="chartData"
      :options="chartOptions"
    />
  </div>
</template>
