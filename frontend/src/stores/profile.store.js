import { defineStore } from 'pinia'

import {
  profileService,
} from '@/services/profile.service'

export const useProfileStore =
  defineStore('profile', {
    state: () => ({
      profile: null,

      loading: false,
    }),

    actions: {
      async fetchProfile() {
        this.loading = true

        try {
          const { data } =
            await profileService.getProfile()

          this.profile =
            data
        } finally {
          this.loading = false
        }
      },

      async updateProfile(
        payload
      ) {
        const { data } =
          await profileService.updateProfile(
            payload
          )

        this.profile =
          data
      },

      async changePassword(
        payload
      ) {
        await profileService.changePassword(
          payload
        )
      },
    },
  })
