// Action Types

const GET_BIZ = "biz/get-all-biz"
const GET_USERS_BIZ = "biz/get-user-biz"

const CREATE_BIZ = "biz/create-biz"
const READ_BIZ = "biz/read-biz"
const UPDATE_BIZ = "biz/update-biz"
const DELETE_BIZ = "biz/delete-biz"

// Action Creators

const getBizAction = payload => {
    return {
        type: GET_BIZ,
        payload
    }
}

const getUsersBizAction = payload => {
    return {
        type: GET_USERS_BIZ,
        payload
    }
}

const createBizAction = payload => {
    return {
        type: CREATE_BIZ,
        payload
    }
}

const readBizAction = payload => {
    return {
        type: READ_BIZ,
        payload
    }
}

const updateBizAction = payload => {
    return {
        type: UPDATE_BIZ,
        payload
    }
}

const deleteBizAction = payload => {
    return {
        type: DELETE_BIZ,
        payload
    }
}

// Thunk Action Creators

// Reducer

const intitialState = {}

const businessReducer = (state = intitialState, action) => {
    let newState = {...state};
    switch (action.type) {
        case (GET_BIZ): {
            action.payload.Businesses.forEach(business => {
                newState[business.id] = { ...newState[business.id], ...business }
            })
            return newState
        }
        case (GET_USERS_BIZ): {
            action.payload.Businesses.forEach(business => {
                newState[business.id] = { ...newState[business.id], ...business }
            })
            return newState
        }
        case (CREATE_BIZ): {
            newState[action.payload.id] = action.payload
            return newState
        }
        case (READ_BIZ): {
            newState[action.payload.id] = { ...newState[action.payload.id], ...action.payload }
            return newState
        }
        case (UPDATE_BIZ): {
            newState[action.payload.id] = { ...newState[action.payload.id], ...action.payload }
            return newState
        }
        case (DELETE_BIZ): {
            delete newState[action.payload]
            return newState
        }
        default: {
            return state
        }
    }
}

export default businessReducer
