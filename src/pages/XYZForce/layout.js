


import React from 'react'
import ReactDOM from 'react-dom'
import { Canvas, extend, useThree } from 'react-three-fiber'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'
import './styles.css'

extend({ OrbitControls })

const Cube = () => {
    return (
        <mesh>
            <boxBufferGeometry attach="geometry" />
            <meshBasicMaterial attach="material" color="hotpink" opacity={0.5} transparent />
        </mesh>
    )
}

const XYZForce = () => {
    const {
        camera,
        gl: { domElement }
    } = useThree()
    return (
        <>
            <Cube />
            <orbitControls args={[camera, domElement]} />
        </>
    )
}

export default XYZForce