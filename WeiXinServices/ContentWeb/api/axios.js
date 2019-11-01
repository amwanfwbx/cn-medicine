/** axios封装
 * 请求拦截、相应拦截、错误统一处理
 */
import Vue from 'vue'
import axios from 'axios'

axios.defaults.withCredentials = true
//axios.defaults.baseURL = process.env.VUE_APP_API_URL
axios.defaults.baseURL = "http://localhost:3080"

Vue.prototype.$axios = axios



// 全局请求的入口
export const request = (opt) => {
    return axios(opt);
}

/**
 * @name: goGet
 * @msg: get请求
 * @data {type} (String url, Object data)
 * @return: promise
 */
export const goGet = (url, data = {}) => {
    return request({
        method: 'GET',
        url,
        params: data
    });
}

/**
 * @name: goPost
 * @msg: post请求
 * @param {type} (String url, Object data)
 * @return: promise
 */
export const goPost = (url, data = {}, options) => {
  return request({
    method: 'POST',
    url,
    data
  }, options)
}

/**
 * @name: goPut
 * @msg: put请求
 * @param {type} (String url, Object data)
 * @return: promise
 */
export const goPut = (url, data = {}, options) => {
  return request({
    method: 'PUT',
    url,
    data
  }, options)
}

/**
 * @name: goDelete
 * @msg: delete请求
 * @param {type} (String url, Object data)
 * @return: promise
 */
export const goDelete = (url, data = {}, options) => {
  return request({
    method: 'DELETE',
    url,
    data
  }, options)
}

/**
 * @name: goPatch
 * @msg: PATCH请求
 * @param {type} (String url, Object data)
 * @return: promise
 */
export const goPatch = (url, data = {}, options) => {
  return request({
    method: 'PATCH',
    url,
    data
  }, options)
}
