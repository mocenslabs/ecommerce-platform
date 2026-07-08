import api from './api'

export const profileService = {
  getProfile() {
    return api.get(
      '/users/profile/'
    )
  },

  updateProfile(
    payload
  ) {
    return api.patch(
      '/users/profile/',
      payload
    )
  },

  changePassword(
    payload
  ) {
    return api.post(
      '/users/change-password/',
      payload
    )
  },
}
