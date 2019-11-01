import { goGet } from './axios'

export const logout = () => goGet(`${process.env.VUE_APP_PUBLIC_SERVER}/auth/uac/logout`, null, { showMessage: false })

export const check = (params) => goGet(`${process.env.VUE_APP_PUBLIC_SERVER}/auth/check`, params, { showLoading: false, showMessage: false })

export const getUser = () => goGet(`${process.env.VUE_APP_PUBLIC_SERVER}/auth/user`, null, { showLoading: false, showMessage: false })

export const getCode = (params) => goGet(`${process.env.VUE_APP_PUBLIC_SERVER}/auth/uac/code`, params, { showLoading: true, showMessage: true })
