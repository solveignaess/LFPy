#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyright (C) 2012 Computational Neuroscience Group, NMBU.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

"""

from __future__ import division
import unittest
import os
import numpy as np
import LFPy


class testMEG(unittest.TestCase):
    """
    test class LFPy.MEG
    """

    def test_MEG_00(self):
        '''test LFPy.MEG.calculate_H()'''
        current_dipole_moment = np.zeros((11, 3))
        current_dipole_moment[:, 0] += 1.
        dipole_location = np.zeros(3)
        sensor_locations = np.r_[np.eye(3), -np.eye(3)]

        gt = np.zeros((sensor_locations.shape[0],
                       current_dipole_moment.shape[0], 3))
        gt[1, :, 2] = 1./4/np.pi
        gt[2, :, 1] = -1./4/np.pi
        gt[4, :, 2] = -1./4/np.pi
        gt[5, :, 1] = 1./4/np.pi

        meg = LFPy.MEG(sensor_locations)
        np.testing.assert_equal(gt, meg.calculate_H(current_dipole_moment,
                                                    dipole_location))

    def test_MEG_01(self):
        '''test LFPy.MEG.calculate_H()'''
        current_dipole_moment = np.zeros((11, 3))
        current_dipole_moment[:, 1] += 1.
        dipole_location = np.zeros(3)
        sensor_locations = np.r_[np.eye(3), -np.eye(3)]

        gt = np.zeros((sensor_locations.shape[0],
                       current_dipole_moment.shape[0], 3))
        gt[0, :, 2] = -1./4/np.pi
        gt[2, :, 0] = 1./4/np.pi
        gt[3, :, 2] = 1./4/np.pi
        gt[5, :, 0] = -1./4/np.pi

        meg = LFPy.MEG(sensor_locations)
        np.testing.assert_equal(gt, meg.calculate_H(current_dipole_moment,
                                                    dipole_location))

    def test_MEG_02(self):
        '''test LFPy.MEG.calculate_H()'''
        current_dipole_moment = np.zeros((11, 3))
        current_dipole_moment[:, 2] += 1.
        dipole_location = np.zeros(3)
        sensor_locations = np.r_[np.eye(3), -np.eye(3)]

        # ground truth
        gt = np.zeros((sensor_locations.shape[0],
                       current_dipole_moment.shape[0], 3))
        gt[0, :, 1] = 1./4/np.pi
        gt[1, :, 0] = -1./4/np.pi
        gt[3, :, 1] = -1./4/np.pi
        gt[4, :, 0] = 1./4/np.pi

        meg = LFPy.MEG(sensor_locations)
        np.testing.assert_equal(gt, meg.calculate_H(current_dipole_moment,
                                                    dipole_location))

    def test_MEG_03(self):
        '''test LFPy.MEG.calculate_H()'''
        current_dipole_moment = np.zeros((1, 3))
        current_dipole_moment[:, 0] += 1.
        dipole_location = np.zeros(3)
        sensor_locations = np.r_[np.eye(3), -np.eye(3)]

        gt = np.zeros((sensor_locations.shape[0],
                       current_dipole_moment.shape[0], 3))
        gt[1, :, 2] = 1./4/np.pi
        gt[2, :, 1] = -1./4/np.pi
        gt[4, :, 2] = -1./4/np.pi
        gt[5, :, 1] = 1./4/np.pi

        meg = LFPy.MEG(sensor_locations)
        np.testing.assert_equal(gt, meg.calculate_H(current_dipole_moment,
                                                    dipole_location))

    def test_MEG_04(self):
        '''test LFPy.MEG.calculate_H()'''
        current_dipole_moment = np.zeros((1, 3))
        current_dipole_moment[:, 1] += 1.
        dipole_location = np.zeros(3)
        sensor_locations = np.r_[np.eye(3), -np.eye(3)]

        gt = np.zeros((sensor_locations.shape[0],
                       current_dipole_moment.shape[0], 3))
        gt[0, :, 2] = -1./4/np.pi
        gt[2, :, 0] = 1./4/np.pi
        gt[3, :, 2] = 1./4/np.pi
        gt[5, :, 0] = -1./4/np.pi

        meg = LFPy.MEG(sensor_locations)
        np.testing.assert_equal(gt, meg.calculate_H(current_dipole_moment,
                                                    dipole_location))

    def test_MEG_05(self):
        '''test LFPy.MEG.calculate_H()'''
        current_dipole_moment = np.zeros((1, 3))
        current_dipole_moment[:, 2] += 1.
        dipole_location = np.zeros(3)
        sensor_locations = np.r_[np.eye(3), -np.eye(3)]

        gt = np.zeros((sensor_locations.shape[0],
                       current_dipole_moment.shape[0], 3))
        gt[0, :, 1] = 1./4/np.pi
        gt[1, :, 0] = -1./4/np.pi
        gt[3, :, 1] = -1./4/np.pi
        gt[4, :, 0] = 1./4/np.pi

        meg = LFPy.MEG(sensor_locations)
        np.testing.assert_equal(gt, meg.calculate_H(current_dipole_moment,
                                                    dipole_location))


class testFourSphereVolumeConductor(unittest.TestCase):
    """
    test class LFPy.FourSphereVolumeConductor
    """

    def test_decompose_dipole(self):
        '''Test radial and tangential parts of dipole sums to dipole'''
        P1 = np.array([[1., 1., 1.]])
        p_rad, p_tan = decompose_dipole(P1)
        np.testing.assert_equal(p_rad + p_tan, P1)

    def test_rad_dipole(self):
        '''Test that radial part of decomposed dipole is correct'''
        P1 = np.array([[1., 1., 1.]])
        p_rad, p_tan = decompose_dipole(P1)
        np.testing.assert_equal(p_rad, np.array([[0., 0., 1.]]))

    def test_tan_dipole(self):
        '''Test that tangential part of decomposed dipole is correct'''
        P1 = np.array([[1., 1., 1.]])
        p_rad, p_tan = decompose_dipole(P1)
        np.testing.assert_equal(p_tan, np.array([[1., 1., 0.]]))

    def test_calc_theta(self):
        '''Test theta: angle between rz and r'''
        rz1 = np.array([0., 0., 70.])
        r_el = np.array([[0., 0., 90.], [0., 0., -90.],[0., 70., 0.], [0., -70., 0.], [0., 10., 10.]])
        fs = make_class_object(rz1, r_el)
        theta = fs.calc_theta()
        np.testing.assert_almost_equal(theta, np.array([0., np.pi, np.pi/2, np.pi/2, np.pi/4]))

    def test_calc_phi(self):
        '''Test phi: azimuthal angle between rx and rxy'''
        rz1 = np.array([0., 0., 70.])
        r_el = np.array([[0., 1., 0], [-1., -1., 1.],[1., 1., 4.]])
        fs = make_class_object(rz1, r_el)
        P1 = np.array([[0., 1., 0.], [1., 0., 1.]])
        phi = fs.calc_phi(P1)
        np.testing.assert_almost_equal(phi, np.array([[np.pi/2, np.pi], [5*np.pi/4, 7*np.pi/4], [np.pi/4, 3*np.pi/4]]))

    def test_rad_sign(self):
        '''Test if radial dipole points inwards or outwards'''
        rz1 = np.array([0., 0., 70.])
        r_el = np.array([[0., 0., 90.]])
        fs = make_class_object(rz1, r_el)
        P1 = np.array([[0., 0., 1.], [0., 0., -2.]])
        s_vector = fs._sign_rad_dipole(P1)
        np.testing.assert_almost_equal(s_vector, np.array([1., -1.]))

    def test_calc_vn(self):
        '''test that calc_vn gives correct values'''
        n = 1
        fs = make_simple_class_object()
        v1 = fs._calc_vn(1)
        np.testing.assert_almost_equal(v1, -4.75)

    def test_calc_yn(self):
        '''test that calc_yn gives correct values'''
        n = 1
        fs = make_simple_class_object()
        y1 = fs._calc_yn(1)
        np.testing.assert_almost_equal(y1, -2.3875)

    def test_calc_zn(self):
        '''test that calc_zn gives correct values'''
        n = 1
        fs = make_simple_class_object()
        z1 = fs._calc_zn(1)
        np.testing.assert_almost_equal(z1, -2.16574585635359)

    def test_calc_potential(self):
        '''test comparison between four-sphere model and model for
        infinite homogeneous space
        when sigma is constant and r4 goes to infinity'''
        sigmas = [0.3, 0.3, 0.3+1e-16, 0.3]
        radii = [10., 20*1e6, 30.*1e6, 40.*1e6]
        rz = np.array([0., 0., 3.])
        p = np.array([[0., 0., 100.], [50., 50., 0.]])
        r_elec = np.array([[0., 0., 9.],
                           [0., 0., 15.],
                           [0., 0., 25.],
                           [0., 0., 40.],
                           [0., 9., 0.],
                           [0., 15., 0.],
                           [0., 25., 0.],
                           [0., 40., 0.]])
        four_s = LFPy.FourSphereVolumeConductor(radii, sigmas, r_elec, rz)
        pots_4s = four_s.calc_potential(p)
        inf_s = LFPy.InfiniteVolumeConductor(0.3)
        pots_inf = inf_s.get_dipole_potential(p, r_elec - rz)

        np.testing.assert_allclose(pots_4s, pots_inf, rtol=1e-6)


class testInfiniteVolumeConductor(unittest.TestCase):
    """
    test class InfiniteVolumeConductor
    """
    def test_get_dipole_potential(self):
        sigma = 0.3
        r = np.array([[0., 0., 1.], [0., 1., 0.]])
        p = np.array([[0., 0., 4*np.pi*0.3], [0., 4*np.pi*0.3, 0.]])
        inf_model = LFPy.InfiniteVolumeConductor(sigma)
        phi = inf_model.get_dipole_potential(p, r)
        np.testing.assert_allclose(phi, np.array([[1., 0.], [0., 1.]]))


class testOneSphereVolumeConductor(unittest.TestCase):
    """
    test class OneSphereVolumeConductor
    """
    def test_OneSphereVolumeConductor_00(self):
        """test case where sigma_i == sigma_o which
        should be identical to the standard point-source potential in
        infinite homogeneous media
        """
        # current magnitude
        I = 1.
        # conductivity
        sigma = 0.3 
        # sphere radius
        R = 1000
        # source location (along x-axis)
        rs = 800
        # sphere coordinates of observation points
        radius = np.r_[np.arange(0, rs), np.arange(rs+1, rs*2)]
        theta = np.zeros(radius.shape)
        phi = np.zeros(radius.shape)
        r = np.array([radius, theta, phi])
        
        # predict potential
        sphere = LFPy.OneSphereVolumeConductor(r=r, R=R, sigma_i=sigma, sigma_o=sigma)
        phi = sphere.calc_potential(rs=rs, I=I)
        
        # ground truth
        phi_gt = I / (4*np.pi*sigma*abs(radius-rs))
        
        # test
        np.testing.assert_almost_equal(phi, phi_gt)

    def test_OneSphereVolumeConductor_01(self):
        """test case where sigma_i == sigma_o which
        should be identical to the standard point-source potential in
        infinite homogeneous media
        """
        # current magnitude
        I = np.ones(10)
        # conductivity
        sigma = 0.3 
        # sphere radius
        R = 1000
        # source location (along x-axis)
        rs = 800
        # sphere coordinates of observation points
        radius = np.r_[np.arange(0, rs), np.arange(rs+1, rs*2)]
        theta = np.zeros(radius.shape)
        phi = np.zeros(radius.shape)
        r = np.array([radius, theta, phi])
        
        # predict potential
        sphere = LFPy.OneSphereVolumeConductor(r=r, R=R, sigma_i=sigma, sigma_o=sigma)
        phi = sphere.calc_potential(rs=rs, I=I)
        
        # ground truth
        phi_gt = I[0] / (4*np.pi*sigma*abs(radius-rs))
        
        # test
        np.testing.assert_almost_equal(phi, np.array([phi_gt]*I.size).T)

    def test_OneSphereVolumeConductor_02(self):
        """test case where sigma_i == sigma_o which
        should be identical to the standard point-source potential in
        infinite homogeneous media
        """
        # current magnitude
        I = 1.
        # conductivity
        sigma = 0.3 
        # sphere radius
        R = 10000
        # cell body position
        xs = 8000.
        # sphere coordinates of observation points
        radius = np.r_[np.arange(0, xs), np.arange(xs+1, xs*2)][::10]
        theta = np.zeros(radius.shape)+np.pi/2
        phi = np.zeros(radius.shape)
        r = np.array([radius, theta, phi])
        # set up cell        
        cell = LFPy.Cell(morphology=os.path.join(LFPy.__path__[0], 'test', 'stick.hoc'))
        cell.set_pos(x=xs, y=0, z=0)
        cell.set_rotation(y=np.pi/2)
        
        # predict potential
        sphere = LFPy.OneSphereVolumeConductor(r=r, R=R, sigma_i=sigma, sigma_o=sigma)
        mapping = sphere.calc_mapping(cell=cell, n_max=100)
                
        # ground truth and tests
        for i, x in enumerate(cell.xmid):
            dist = radius-x
            dist[abs(dist) < cell.diam[i]] = cell.diam[i]
            phi_gt = I / (4*np.pi*sigma*abs(dist))
            np.testing.assert_almost_equal(mapping[:, i], phi_gt)



######## Functions used by tests: ##############################################

def make_class_object(rz1, r_el):
    '''Return class object fs'''
    radii = [79., 80., 85., 90.]
    sigmas = [0.3, 0.015, 15, 0.3]
    fs = LFPy.FourSphereVolumeConductor(radii, sigmas, r_el, rz1)
    return fs

def make_simple_class_object():
    '''Return class object fs'''
    radii = [1., 2., 4., 8.]
    sigmas = [1., 2., 4., 8.]
    rz1 = np.array([0., 0., .9])
    r_el = np.array([[0., 0., 1.5]])
    fs = LFPy.FourSphereVolumeConductor(radii, sigmas, r_el, rz1)
    return fs

def decompose_dipole(P1):
    '''Return decomposed current dipole'''
    rz1 = np.array([0., 0., 70.])
    r_el = np.array([[0., 0., 90.]])
    fs = make_class_object(rz1, r_el)
    p_rad, p_tan = fs._decompose_dipole(P1)
    return p_rad, p_tan
