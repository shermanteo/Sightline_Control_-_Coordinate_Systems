function [q0, q1, q2, q3] =  RotationMatrix2quaternion (R)
% Description: Converting the rotation matrix to quaternions
% A quaternion is represented by four elements: q0+iq1+jq2+kq3, where q0, 
% q1, q2 and q3 are real numbers, and i, j and k are mutually orthogonal 
% imaginary unit vectors
%
% Input Parameters
% Rotation Matrix which is provided that can be converted to quaternions 
% using 2 steps. First step is to find the magnitude of each quaternion 
% component. This leaves the sign of each component undefined. Second step 
% is to resolve the signs, find the largest of q0, q1, q2, q3 and assume 
% its sign is positive. Then compute the remaining components as shown in 
% the table below. Taking the largest magnitude avoids division by small 
% numbers, which would reduce numerical accuracy.
%
% Output Parameters
% q0 = q0 term is referred to as the "real" component
% q1 = q1 term is referred to as the "imaginary" component
% q2 = q2 term is referred to as the "imaginary" component
% q3 = q3 term is referred to as the "imaginary" component
%

% Step 1: Find the magnitude of each quaternion component. This leaves the 
% sign of each component undefined:
q0 = sqrt((1+R(1,1)+R(2,2)+R(3,3))/4);
q1 = sqrt((1+R(1,1)-R(2,2)-R(3,3))/4);
q2 = sqrt((1-R(1,1)+R(2,2)-R(3,3))/4);
q3 = sqrt((1-R(1,1)-R(2,2)+R(3,3))/4);
