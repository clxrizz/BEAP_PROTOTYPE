# Script to generate complete updated index.html with all requested features
import os

html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EM Services - BEAP Lift Servicing Portal (Form 12b)</title>
    <link rel="stylesheet" href="proto.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>

    <!-- Prototype Top Global Switcher (Quick Role & Viewport Mode) -->
    <div class="proto-top-nav">
        <div class="proto-brand">
            <i class="fa-solid fa-elevator"></i>
            <span>BEAP Prototype</span>
            <span class="tag">Form 12b</span>
        </div>
        <div class="proto-controls">
            <span style="font-size:0.68rem; color:#94a3b8;">Switch Role:</span>
            <div class="role-switcher-pills">
                <button type="button" class="role-pill" data-role="welcome" title="Welcome Screen">
                    <i class="fa-solid fa-door-open"></i> Welcome
                </button>
                <button type="button" class="role-pill manager" data-role="manager" title="Estate Manager">
                    <i class="fa-solid fa-user-tie"></i> Estate Manager
                </button>
                <button type="button" class="role-pill contractor" data-role="contractor" title="Lift Contractor">
                    <i class="fa-solid fa-screwdriver-wrench"></i> Lift Contractor
                </button>
                <button type="button" class="role-pill inspector" data-role="inspector" title="EMS Inspector">
                    <i class="fa-solid fa-clipboard-check"></i> EMS Inspector
                </button>
                <button type="button" class="role-pill resident" data-role="resident" title="Resident">
                    <i class="fa-solid fa-house-user"></i> Resident
                </button>
            </div>
            <div class="view-mode-toggle">
                <button type="button" id="btnViewMobile" class="active">Mobile</button>
                <button type="button" id="btnViewDesktop">Laptop</button>
            </div>
        </div>
    </div>

    <!-- App Wrapper / Mobile & Laptop Container -->
    <div class="app-wrapper" id="appWrapper">
        <div class="mobile-container">
            <!-- EM Services Brand Header -->
            <header class="app-header">
                <div class="brand-text-logo">EM SERVICES</div>
                <div class="header-actions">
                    <div id="userHeaderBadge" class="user-current-badge" style="display:none;">
                        <span id="headerRoleName">Estate Manager</span>
                    </div>
                    <button type="button" class="header-logout-btn" id="headerLogoutBtn" style="display:none;">
                        <i class="fa-solid fa-arrow-right-from-bracket"></i> Logout
                    </button>
                </div>
            </header>

            <!-- App Scrollable Main Content -->
            <main class="app-content">

                <!-- 1. ZELEN FIGMA: 01 WELCOME SCREEN -->
                <div id="view-welcome" class="screen-view active">
                    <div class="welcome-portal-wrap">
                        <h1 class="welcome-portal-title">Welcome to EM Services</h1>
                        <p class="welcome-portal-subtitle">Lift Inspection & Estate Management Portal</p>

                        <div class="portal-cards-grid">
                            <div class="portal-selection-card">
                                <div class="portal-icon-box resident-icon">
                                    <i class="fa-solid fa-house"></i>
                                </div>
                                <h2>Resident Portal</h2>
                                <p>Access resident services, track reports, and view lift updates in your block.</p>
                                <button type="button" class="btn-portal" id="btnGoResidentLogin">Resident Login</button>
                            </div>

                            <div class="portal-selection-card">
                                <div class="portal-icon-box org-icon">
                                    <i class="fa-solid fa-building"></i>
                                </div>
                                <h2>Organisation Portal</h2>
                                <p>Secure access for EMS Inspectors, Contractors and Estate Managers.</p>
                                <button type="button" class="btn-portal" id="btnGoOrgLogin">Organisation Login</button>
                            </div>
                        </div>

                        <div style="font-size:0.65rem; color:#94a3b8; text-align:center; line-height:1.4;">
                            Prototype for IT2827 BEAP • 12b Lift Inspection Spot-Check • Authentication & Role-Based Authorisation
                        </div>
                    </div>
                </div>

                <!-- 2. ZELEN FIGMA: ORGANISATION LOGIN SCREEN -->
                <div id="view-org-login" class="screen-view">
                    <div class="figma-auth-card">
                        <div class="figma-auth-header">
                            <h2>Organisation Login</h2>
                            <p>Secure access for authorised personnel.</p>
                        </div>

                        <form id="formOrgLogin" style="display:flex; flex-direction:column; gap:12px;">
                            <div class="figma-field-group">
                                <label>Organisation email address</label>
                                <input type="email" id="inputOrgEmail" class="figma-input" placeholder="name@organisation.com" value="inspector@emservices.sg" required>
                            </div>

                            <button type="submit" class="btn-primary-blue">Continue with SSO</button>

                            <div style="font-size:0.72rem; color:var(--text-secondary); line-height:1.4; background:#f8fafc; padding:8px 10px; border-radius:8px; border:1px solid #e2e8f0;">
                                Your role is assigned by an administrator and checked by the system after you sign in. It cannot be selected or changed here.
                            </div>

                            <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.74rem;">
                                <a href="#" id="linkActivateAccount" style="color:#0263b3; text-decoration:none; font-weight:600;">Activate Invited Account</a>
                                <a href="#" id="linkBackWelcomeFromOrg" style="color:var(--text-secondary); text-decoration:none;">Back to Welcome</a>
                            </div>
                        </form>

                        <div class="proto-demo-box">
                            <span class="proto-demo-title">PROTOTYPE DEMO ONLY • QUICK SELECT ROLE</span>
                            <div class="demo-chips-list">
                                <button type="button" class="demo-chip-btn" onclick="startMfaFlow('manager', 'estatemanager@emservices.sg')">
                                    <span>Estate Manager</span>
                                    <span class="role-tag" style="background:#eff6ff; color:#2563eb;">2FA / MFA</span>
                                </button>
                                <button type="button" class="demo-chip-btn" onclick="startMfaFlow('contractor', 'contractor@mitsubishi.sg')">
                                    <span>Lift contractor (Mitsubishi LC)</span>
                                    <span class="role-tag" style="background:#fffbeb; color:#f59e0b;">2FA / MFA</span>
                                </button>
                                <button type="button" class="demo-chip-btn" onclick="startMfaFlow('inspector', 'inspector.wb@emservices.sg')">
                                    <span>EMS Inspector (Wee Boon)</span>
                                    <span class="role-tag" style="background:#ecfdf5; color:#10b981;">2FA / MFA</span>
                                </button>
                                <button type="button" class="demo-chip-btn" onclick="showScreen('access-denied')">
                                    <span>Unauthorized User Demo</span>
                                    <span class="role-tag" style="background:#fef2f2; color:#ef4444;">Error 403</span>
                                </button>
                                <button type="button" class="demo-chip-btn" onclick="showScreen('session-expired')">
                                    <span>Session Timeout Demo</span>
                                    <span class="role-tag" style="background:#f1f5f9; color:#475569;">13 Expired</span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 2b. ZELEN FIGMA: ORGANISATION SSO SIMULATOR SCREEN -->
                <div id="view-org-sso" class="screen-view">
                    <div class="figma-auth-card">
                        <div class="figma-auth-header">
                            <h2>Organisation SSO</h2>
                            <p>Sign in with your organisation account. This screen simulates an identity provider.</p>
                        </div>

                        <form id="formOrgSSOSubmit" style="display:flex; flex-direction:column; gap:12px;">
                            <div class="figma-field-group">
                                <label>Organisation email address</label>
                                <input type="email" id="ssoOrgEmail" class="figma-input" value="inspector@emservices.demo" required>
                            </div>

                            <div class="figma-field-group">
                                <label>Password</label>
                                <div class="password-wrap">
                                    <input type="password" id="inputSsoPw" class="figma-input" value="DemoPassword#2026" required>
                                    <button type="button" class="toggle-show-btn" id="btnToggleSsoPw">Show</button>
                                </div>
                            </div>

                            <button type="submit" class="btn-primary-blue">Sign In</button>
                            <button type="button" class="btn-secondary-outline" id="btnCancelSSO">Cancel</button>

                            <div style="font-size:0.7rem; color:var(--text-secondary); text-align:center; line-height:1.4;">
                                Your password is handled by your organisation's identity provider and is never stored by EM Services.
                            </div>

                            <div style="text-align:center; font-size:0.74rem;">
                                <a href="#" onclick="showScreen('forgot-pwd'); return false;" style="color:#0263b3; text-decoration:none;">Forgot your organisation password?</a>
                            </div>
                        </form>
                    </div>
                </div>

                <!-- 2c. ZELEN FIGMA: ACTIVATE INVITED ACCOUNT SCREEN -->
                <div id="view-activate-invite" class="screen-view">
                    <div class="figma-auth-card">
                        <div class="figma-auth-header">
                            <h2>Activate Invited Account</h2>
                            <p>New organisation accounts must be invited or approved by an administrator. Enter the details from your invitation.</p>
                        </div>

                        <div id="inviteErrorBox" class="alert-box danger" style="display:none;">
                            <i class="fa-solid fa-circle-exclamation"></i>
                            <span>This invitation is invalid or has expired. Contact your administrator to request a new invitation.</span>
                        </div>

                        <form id="formVerifyInvitation" style="display:flex; flex-direction:column; gap:12px;">
                            <div class="figma-field-group">
                                <label>Organisation email address</label>
                                <input type="email" id="inputInviteEmail" class="figma-input" placeholder="name@organisation.com" value="new.user@emservices.sg" required>
                            </div>

                            <div class="figma-field-group">
                                <label>Invitation code</label>
                                <input type="text" id="inputInviteCode" class="figma-input" placeholder="e.g. EMS-7K3Q-82XD" value="EMS-7K3Q-82XD" required>
                                <span id="inviteCodeErrorNote" style="display:none; font-size:0.68rem; color:#ef4444;">Invitation code not recognised or no longer valid.</span>
                            </div>

                            <button type="submit" class="btn-primary-blue">Verify Invitation</button>

                            <div style="text-align:center; font-size:0.74rem;">
                                <a href="#" onclick="showScreen('org-login'); return false;" style="color:var(--text-secondary); text-decoration:none;">Back to Organisation Login</a>
                            </div>
                        </form>

                        <div class="proto-demo-box">
                            <span class="proto-demo-title">PROTOTYPE DEMO ONLY</span>
                            <button type="button" class="demo-chip-btn" id="btnToggleInvalidInviteDemo">
                                <span>Toggle Invalid / Expired Code State</span>
                                <span class="role-tag" style="background:#fee2e2; color:#b91c1c;">11b State</span>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- 3. ZELEN FIGMA: 2-FACTOR AUTHENTICATION / VERIFY YOUR EMAIL -->
                <div id="view-mfa" class="screen-view">
                    <div class="figma-auth-card">
                        <div class="figma-auth-header">
                            <h2>Verify Your Email</h2>
                            <p>We sent a 6-digit verification code to <span id="mfaEmailTarget" style="font-weight:700; color:#0263b3;">inspector@emservices.sg</span>. Enter it below to activate your session.</p>
                        </div>

                        <div id="mfaExpiredAlert" class="alert-box danger" style="display:none;">
                            <i class="fa-solid fa-circle-exclamation"></i>
                            <span>This code has expired. Request a new code to continue.</span>
                        </div>

                        <form id="formMfaVerify" style="display:flex; flex-direction:column; gap:12px;">
                            <div class="mfa-code-grid">
                                <input type="text" maxlength="1" class="mfa-digit-box" value="3" autofocus>
                                <input type="text" maxlength="1" class="mfa-digit-box" value="9">
                                <input type="text" maxlength="1" class="mfa-digit-box" value="5">
                                <input type="text" maxlength="1" class="mfa-digit-box" value="1">
                                <input type="text" maxlength="1" class="mfa-digit-box" value="6">
                                <input type="text" maxlength="1" class="mfa-digit-box" value="0">
                            </div>

                            <button type="submit" class="btn-primary-blue">
                                <i class="fa-solid fa-check"></i> Verify
                            </button>
                            <button type="button" class="btn-secondary-outline" id="btnCancelMfa">Cancel</button>

                            <div style="text-align:center; font-size:0.72rem; margin-top:2px;">
                                Didn't receive a code? <a href="#" id="linkResendMfaCode" style="color:#0263b3; text-decoration:none; font-weight:600;">Resend Code</a>
                            </div>
                        </form>

                        <div class="proto-demo-box">
                            <span class="proto-demo-title">PROTOTYPE DEMO ONLY</span>
                            <button type="button" class="demo-chip-btn" id="btnToggleMfaExpiredDemo">
                                <span>Toggle Expired Code Error Banner</span>
                                <span class="role-tag" style="background:#fee2e2; color:#b91c1c;">Expired Demo</span>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- 4. ZELEN FIGMA: 02 RESIDENT LOGIN SCREEN -->
                <div id="view-resident-login" class="screen-view">
                    <div class="figma-auth-card">
                        <div class="figma-auth-header">
                            <h2>Resident Login</h2>
                            <p>Sign in to access resident services and lift status in your block.</p>
                        </div>

                        <form id="formResidentLogin" style="display:flex; flex-direction:column; gap:12px;">
                            <div class="figma-field-group">
                                <label>Email address</label>
                                <input type="email" id="inputResidentEmail" class="figma-input" placeholder="name@example.com" value="resident@woodlands.sg" required>
                            </div>

                            <div class="figma-field-group">
                                <label>Password</label>
                                <div class="password-wrap">
                                    <input type="password" id="inputResidentPw" class="figma-input" value="Resident#2026" required>
                                    <button type="button" class="toggle-show-btn" id="btnToggleResidentPw">Show</button>
                                </div>
                            </div>

                            <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.72rem;">
                                <label style="display:flex; align-items:center; gap:6px; cursor:pointer;">
                                    <input type="checkbox" checked style="accent-color:#0263b3;"> Remember me
                                </label>
                                <a href="#" id="linkGoForgotPw" style="color:#0263b3; text-decoration:none; font-weight:600;">Forgot Password?</a>
                            </div>

                            <button type="submit" class="btn-primary-blue">Sign In</button>

                            <div style="text-align:center; font-size:0.75rem; color:var(--text-secondary); margin-top:4px;">
                                New to EM Services?
                            </div>

                            <button type="button" class="btn-secondary-outline" id="btnGoResidentSignUp">Create Account</button>

                            <div style="text-align:center; margin-top:4px;">
                                <a href="#" id="linkBackWelcomeFromResident" style="color:var(--text-secondary); font-size:0.74rem; text-decoration:none;">Back to Welcome</a>
                            </div>
                        </form>
                    </div>
                </div>

                <!-- 5. ZELEN FIGMA: 03 RESIDENT SIGN UP (CREATE RESIDENT ACCOUNT) -->
                <div id="view-resident-signup" class="screen-view">
                    <div class="figma-auth-card">
                        <div class="figma-auth-header">
                            <h2>Create Resident Account</h2>
                            <p>Register to access resident services and view block lift status.</p>
                        </div>

                        <form id="formResidentSignUp" style="display:flex; flex-direction:column; gap:10px;">
                            <div class="figma-field-group">
                                <label>Full Name</label>
                                <input type="text" class="figma-input" placeholder="Enter your full name" value="Daniel Tan" required>
                            </div>

                            <div class="figma-input-row">
                                <div class="figma-field-group">
                                    <label>Address</label>
                                    <input type="text" class="figma-input" placeholder="Street address" value="Woodlands St 53" required>
                                </div>
                                <div class="figma-field-group">
                                    <label>Block</label>
                                    <input type="text" class="figma-input" placeholder="e.g. 554" value="554" required>
                                </div>
                            </div>

                            <div class="figma-input-row">
                                <div class="figma-field-group">
                                    <label>Unit Number</label>
                                    <input type="text" class="figma-input" placeholder="e.g. #08-123" value="#09-241" required>
                                </div>
                                <div class="figma-field-group">
                                    <label>Postal Code</label>
                                    <input type="text" class="figma-input" placeholder="6-digit postal" value="730554" required>
                                </div>
                            </div>

                            <div class="figma-field-group">
                                <label>Email Address</label>
                                <input type="email" class="figma-input" placeholder="name@example.com" value="daniel.tan@woodlands.sg" required>
                            </div>

                            <div class="figma-field-group">
                                <label>Password</label>
                                <input type="password" id="inputSignupPw" class="figma-input" value="Pass@2026" required>
                                
                                <div class="pwd-strength-meter-wrap">
                                    <div class="pwd-strength-bars">
                                        <div class="pwd-strength-bar active-strong"></div>
                                        <div class="pwd-strength-bar active-strong"></div>
                                        <div class="pwd-strength-bar active-strong"></div>
                                        <div class="pwd-strength-bar active-strong"></div>
                                    </div>
                                    <div class="pwd-strength-label">Password strength: Strong</div>
                                    <div class="pwd-rules-list">
                                        <div class="pwd-rule-item valid"><i class="fa-solid fa-circle-check"></i> At least 8 characters</div>
                                        <div class="pwd-rule-item valid"><i class="fa-solid fa-circle-check"></i> One uppercase letter</div>
                                        <div class="pwd-rule-item valid"><i class="fa-solid fa-circle-check"></i> One number</div>
                                        <div class="pwd-rule-item valid"><i class="fa-solid fa-circle-check"></i> One special character</div>
                                    </div>
                                </div>
                            </div>

                            <div style="font-size:0.72rem; display:flex; align-items:center; gap:6px; margin:4px 0;">
                                <input type="checkbox" checked required style="accent-color:#0263b3;">
                                <span>I agree to the Terms and Conditions</span>
                            </div>

                            <button type="submit" class="btn-primary-blue">Create Account</button>

                            <div style="text-align:center; font-size:0.74rem;">
                                <a href="#" id="linkBackResidentLogin" style="color:#0263b3; text-decoration:none; font-weight:600;">Already have an account? Sign In</a>
                            </div>
                        </form>
                    </div>
                </div>

                <!-- 6. ZELEN FIGMA: 05 FORGOT PASSWORD SCREEN -->
                <div id="view-forgot-pwd" class="screen-view">
                    <div class="figma-auth-card">
                        <div class="figma-auth-header">
                            <h2>Forgot Password</h2>
                            <p>Enter the email address registered to your account and we'll send you a link to reset your password.</p>
                        </div>

                        <form id="formForgotPwd" style="display:flex; flex-direction:column; gap:12px;">
                            <div class="figma-field-group">
                                <label>Registered email address</label>
                                <input type="email" id="inputForgotEmail" class="figma-input" placeholder="name@example.com" value="resident@woodlands.sg" required>
                            </div>

                            <button type="submit" class="btn-primary-blue">Send Reset Link</button>

                            <div style="text-align:center; margin-top:6px;">
                                <a href="#" id="linkBackLoginFromForgot" style="color:#0263b3; font-size:0.74rem; text-decoration:none; font-weight:600;">Back to Login</a>
                            </div>
                        </form>
                    </div>
                </div>

                <!-- 7. ZELEN FIGMA: CHECK YOUR EMAIL SCREEN -->
                <div id="view-check-email" class="screen-view">
                    <div class="figma-auth-card" style="text-align:center;">
                        <div class="figma-auth-header">
                            <h2>Check Your Email</h2>
                            <p>We've received your request.</p>
                        </div>

                        <div class="alert-box success" style="text-align:left;">
                            <i class="fa-solid fa-circle-check"></i>
                            <span>If this email belongs to an account, a password reset link will be sent shortly. Check your inbox and spam folder.</span>
                        </div>

                        <button type="button" class="btn-primary-blue" id="btnBackLoginFromCheckEmail">
                            Back to Login
                        </button>

                        <div class="proto-demo-box" style="margin-top:12px;">
                            <span class="proto-demo-title">PROTOTYPE DEMO ONLY</span>
                            <button type="button" class="demo-chip-btn" id="btnOpenResetLinkDemo">
                                <span><i class="fa-solid fa-envelope-open-text"></i> Open reset link from email</span>
                                <span class="role-tag" style="background:#eff6ff; color:#0263b3;">Simulate Link</span>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- 8. ZELEN FIGMA: RESET PASSWORD SCREEN -->
                <div id="view-reset-pwd" class="screen-view">
                    <div class="figma-auth-card">
                        <div class="figma-auth-header">
                            <h2>Reset Password</h2>
                            <p>Choose a new password for your account.</p>
                        </div>

                        <form id="formResetPasswordSubmit" style="display:flex; flex-direction:column; gap:12px;">
                            <div class="figma-field-group">
                                <label>New Password</label>
                                <div class="password-wrap">
                                    <input type="password" id="inputNewPw" class="figma-input" value="NewPass@2026" required>
                                    <button type="button" class="toggle-show-btn" id="btnToggleNewPw">Show</button>
                                </div>

                                <div class="pwd-strength-meter-wrap">
                                    <div class="pwd-strength-bars">
                                        <div class="pwd-strength-bar active-strong"></div>
                                        <div class="pwd-strength-bar active-strong"></div>
                                        <div class="pwd-strength-bar active-strong"></div>
                                        <div class="pwd-strength-bar active-strong"></div>
                                    </div>
                                    <div class="pwd-strength-label" id="resetStrengthLabel">Password strength: Strong</div>
                                    <div class="pwd-rules-list">
                                        <div class="pwd-rule-item valid"><i class="fa-solid fa-circle-check"></i> At least 8 characters</div>
                                        <div class="pwd-rule-item valid"><i class="fa-solid fa-circle-check"></i> One uppercase letter</div>
                                        <div class="pwd-rule-item valid"><i class="fa-solid fa-circle-check"></i> One number</div>
                                        <div class="pwd-rule-item valid"><i class="fa-solid fa-circle-check"></i> One special character</div>
                                    </div>
                                </div>
                            </div>

                            <div class="figma-field-group">
                                <label>Confirm New Password</label>
                                <div class="password-wrap">
                                    <input type="password" id="inputConfirmPw" class="figma-input" value="NewPass@2026" required>
                                    <button type="button" class="toggle-show-btn" id="btnToggleConfirmPw">Show</button>
                                </div>
                            </div>

                            <button type="submit" class="btn-primary-blue">Reset Password</button>

                            <div style="text-align:center; margin-top:4px;">
                                <a href="#" id="linkBackLoginFromReset" style="color:var(--text-secondary); font-size:0.74rem; text-decoration:none;">Back to Login</a>
                            </div>
                        </form>
                    </div>
                </div>

                <!-- 9. ZELEN FIGMA: PASSWORD RESET SUCCESSFUL SCREEN -->
                <div id="view-pwd-success" class="screen-view">
                    <div class="figma-auth-card" style="text-align:center; padding:32px 20px;">
                        <div style="width:56px; height:56px; border-radius:50%; background:#dcfce7; color:#16a34a; display:inline-flex; align-items:center; justify-content:center; font-size:1.8rem; margin-bottom:12px;">
                            <i class="fa-solid fa-circle-check"></i>
                        </div>
                        <h2 style="font-size:1.3rem; font-weight:800; color:#0f2b48; margin-bottom:6px;">Password Reset Successful</h2>
                        <p style="font-size:0.78rem; color:var(--text-secondary); margin-bottom:18px;">Your password has been reset successfully.</p>
                        <button type="button" class="btn-primary-blue" id="btnBackToLoginAfterSuccess">Back to Login</button>
                    </div>
                </div>

                <!-- 10. FIGMA: ACCESS DENIED SCREEN (ERROR 403) -->
                <div id="view-access-denied" class="screen-view">
                    <div class="figma-auth-card" style="text-align:center; padding:32px 20px;">
                        <div style="width:56px; height:56px; border-radius:50%; background:#fee2e2; color:#ef4444; display:inline-flex; align-items:center; justify-content:center; font-size:1.8rem; margin-bottom:12px;">
                            <i class="fa-solid fa-triangle-exclamation"></i>
                        </div>
                        <h2 style="font-size:1.3rem; font-weight:800; color:#0f2b48; margin-bottom:6px;">Access Denied</h2>
                        <p style="font-size:0.78rem; color:var(--text-secondary); line-height:1.5; margin-bottom:12px;">
                            Your account is not authorised to access EM Services. Please contact your administrator.
                        </p>
                        <div style="font-size:0.7rem; color:#94a3b8; margin-bottom:18px;">
                            Error 403 • No active role is assigned to this account
                        </div>
                        <button type="button" class="btn-primary-blue" onclick="showScreen('org-login')">Back to Organisation Login</button>
                    </div>
                </div>

                <!-- 11. FIGMA: 13 SESSION EXPIRED SCREEN -->
                <div id="view-session-expired" class="screen-view">
                    <div class="figma-auth-card" style="text-align:center; padding:32px 20px;">
                        <div style="width:56px; height:56px; border-radius:50%; background:#eff6ff; color:#0263b3; display:inline-flex; align-items:center; justify-content:center; font-size:1.8rem; margin-bottom:12px;">
                            <i class="fa-regular fa-clock"></i>
                        </div>
                        <h2 style="font-size:1.3rem; font-weight:800; color:#0f2b48; margin-bottom:6px;">Session Expired</h2>
                        <p style="font-size:0.78rem; color:var(--text-secondary); line-height:1.5; margin-bottom:20px;">
                            For your security, you were signed out after a period of inactivity. Please sign in again to continue.
                        </p>
                        <button type="button" class="btn-primary-blue" onclick="showScreen('org-login')">Sign In Again</button>
                    </div>
                </div>

                <!-- 12. FIGMA: TASKS - SENT BACK FOR REWORK SCREEN -->
                <div id="view-task-rework" class="screen-view">
                    <div style="margin-bottom:10px;">
                        <button type="button" class="btn-secondary-outline" style="width:auto; display:inline-flex; padding:5px 12px; font-size:0.72rem;" onclick="showScreen('manager'); switchManagerSubView('tasks');">
                            <i class="fa-solid fa-arrow-left"></i> Back to Tasks
                        </button>
                    </div>

                    <div class="alert-box warning" style="background:#fffbeb; border-color:#fde68a; color:#92400e;">
                        <i class="fa-solid fa-triangle-exclamation"></i>
                        <div>
                            <strong>Sent back for rework:</strong> D-0417 - ARD & EBOPS has been returned to Fujitec. Sign-off is paused until they fix it and resubmit.
                        </div>
                    </div>

                    <div class="portal-selection-card" style="text-align:left; align-items:stretch; padding:16px;">
                        <h3 style="font-size:0.95rem; font-weight:800; color:#0f2b48; margin-bottom:8px;">What was sent back</h3>
                        <div style="font-size:0.74rem; display:grid; grid-template-columns:120px 1fr; gap:6px 12px; line-height:1.4;">
                            <span style="color:#64748b;">Task:</span> <strong>(9) ARD & EBOPS - functioning? Replacement date?</strong>
                            <span style="color:#64748b;">Block / Lift:</span> <span>559/A • Woodlands St 54</span>
                            <span style="color:#64748b;">Lift company:</span> <span>Fujitec Singapore</span>
                            <span style="color:#64748b;">Sent back by:</span> <span>A. Lim (Officer-in-charge)</span>
                            <span style="color:#64748b;">Sent back on:</span> <span>04/04/2026, 09:30</span>
                            <span style="color:#64748b;">Reason for rework:</span> <span style="background:#fef2f2; padding:4px 8px; border-radius:4px; color:#b91c1c;">"Battery pack replaced, but the ARD test was not witnessed. Please retest on site and attach new photo evidence."</span>
                            <span style="color:#64748b;">Previous evidence:</span> <span>ard_test.jpg, battery_new.jpg</span>
                            <span style="color:#64748b;">New due date:</span> <strong style="color:#ef4444;">11/04/2026</strong>
                            <span style="color:#64748b;">Photo evidence:</span> <span style="color:#b91c1c; font-weight:700;">New photos required (Major)</span>
                        </div>

                        <div style="margin-top:16px; border-top:1px solid #e2e8f0; padding-top:12px;">
                            <h4 style="font-size:0.8rem; font-weight:700; color:#334155; margin-bottom:8px;">What happens next</h4>
                            <div class="rectification-progress-bar">
                                <div class="progress-step-item">
                                    <div class="step-dot done"></div>
                                    <span>Sent back by officer<br>04/04/2026</span>
                                </div>
                                <div class="progress-step-item">
                                    <div class="step-dot done"></div>
                                    <span>Email sent to Fujitec<br>Due 11/04/2026</span>
                                </div>
                                <div class="progress-step-item">
                                    <div class="step-dot active"></div>
                                    <span>Fujitec reworks & uploads<br>Awaiting resubmit</span>
                                </div>
                                <div class="progress-step-item">
                                    <div class="step-dot"></div>
                                    <span>Back to Awaiting Sign-off</span>
                                </div>
                            </div>
                        </div>

                        <button type="button" class="btn-primary-blue" style="margin-top:16px;" onclick="showScreen('manager'); switchManagerSubView('tasks');">
                            Return to Tasks Table
                        </button>
                    </div>
                </div>

                <!-- ============================================================== -->
                <!-- ROLE 1: ESTATE MANAGER PORTAL (WITH CSV IMPORT/EXPORT)         -->
                <!-- ============================================================== -->
                <div id="view-role-manager" class="screen-view">
                    <div class="dashboard-layout-wrap">
                        <aside class="role-desktop-sidebar manager">
                            <div>
                                <div class="sidebar-group-title">Estate Manager</div>
                                <ul class="sidebar-nav-list">
                                    <li class="sidebar-nav-item">
                                        <button type="button" class="active" onclick="clickRoleTab('manager', 0, 'home', 'Home')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-house"></i> Home</span>
                                        </button>
                                    </li>
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="clickRoleTab('manager', 1, 'tasks', 'Major Defects')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-triangle-exclamation"></i> Major Defects</span>
                                            <span class="sidebar-item-badge" id="managerDefectsBadge">5</span>
                                        </button>
                                    </li>
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="clickRoleTab('manager', 2, 'resident-reports', 'Resident Reports')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-bullhorn"></i> Resident Reports</span>
                                            <span class="sidebar-item-badge">2</span>
                                        </button>
                                    </li>
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="clickRoleTab('manager', 3, 'reports', 'Reports & SLA')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-chart-column"></i> Reports</span>
                                        </button>
                                    </li>
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="clickRoleTab('manager', 4, 'schedule', 'Notifications')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-bell"></i> Notifications</span>
                                        </button>
                                    </li>
                                </ul>
                            </div>
                            <div>
                                <div class="sidebar-group-title">Contacts</div>
                                <ul class="sidebar-nav-list">
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="showToast('EM Services Hotline: 6500 0300')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-phone"></i> Emergency Contact</span>
                                        </button>
                                    </li>
                                </ul>
                            </div>
                        </aside>

                        <div class="dashboard-main-panel">
                            <!-- Subview 1: Manager Home -->
                            <div id="manager-sub-home" class="subview-container active">
                                <div class="role-welcome-banner">
                                    <h1>Welcome, Estate Manager</h1>
                                    <p>Monitor lift performance, track rectification progress, and review reports.</p>
                                    <div class="role-portal-info-box">
                                        <strong>Estate Manager portal:</strong> You are signed in. Your account is authorised to review lift inspections, oversee contractor rectifications, and schedule spot-checks.
                                    </div>
                                </div>

                                <div class="stats-grid" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(130px, 1fr)); gap:10px; margin-bottom:12px;">
                                    <div class="portal-selection-card" style="padding:12px; align-items:flex-start; text-align:left;">
                                        <span style="font-size:0.65rem; color:#64748b; font-weight:700;">TOTAL BLOCK LIFTS</span>
                                        <span style="font-size:1.4rem; font-weight:800; color:#0263b3;">124</span>
                                        <span style="font-size:0.65rem; color:#16a34a;">● 119 Operational</span>
                                    </div>
                                    <div class="portal-selection-card" style="padding:12px; align-items:flex-start; text-align:left;">
                                        <span style="font-size:0.65rem; color:#64748b; font-weight:700;">ACTIVE DEFECTS</span>
                                        <span style="font-size:1.4rem; font-weight:800; color:#ef4444;" id="homeActiveDefectsCount">5 Items</span>
                                        <span style="font-size:0.65rem; color:#d97706;" id="homeAwaitingCount">1 Awaiting Sign-off</span>
                                    </div>
                                    <div class="portal-selection-card" style="padding:12px; align-items:flex-start; text-align:left;">
                                        <span style="font-size:0.65rem; color:#64748b; font-weight:700;">2-WEEK SLA COMPLIANCE</span>
                                        <span style="font-size:1.4rem; font-weight:800; color:#10b981;">96.4%</span>
                                        <span style="font-size:0.65rem; color:#64748b;">Town Council Benchmark</span>
                                    </div>
                                </div>

                                <div style="display:flex; flex-direction:column; gap:8px;">
                                    <span style="font-size:0.75rem; font-weight:700; color:#334155;">Quick actions</span>
                                    <div style="display:flex; gap:8px; flex-wrap:wrap;">
                                        <button type="button" class="btn-primary-blue" style="width:auto;" onclick="clickRoleTab('manager', 1, 'tasks', 'Major Defects')">
                                            <i class="fa-solid fa-list-check"></i> View Active Defects & Rectifications
                                        </button>
                                        <button type="button" class="btn-secondary-outline" style="width:auto;" onclick="openCsvImportModal()">
                                            <i class="fa-solid fa-file-csv"></i> Bulk Import CSV Records
                                        </button>
                                        <button type="button" class="btn-secondary-outline" style="width:auto;" onclick="exportDefectsToCSV()">
                                            <i class="fa-solid fa-download"></i> Export Maintenance CSV
                                        </button>
                                    </div>
                                </div>
                            </div>

                            <!-- Subview 2: Tasks - Active / Awaiting / History with CSV -->
                            <div id="manager-sub-tasks" class="subview-container">
                                <div class="task-header-block">
                                    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
                                        <div>
                                            <h2 style="font-size:1.15rem; font-weight:800; color:#0f2b48;">Tasks Management</h2>
                                            <p style="font-size:0.72rem; color:#64748b;">Defects flagged from failed spot-checks: amend, rectify, then sign off to move them to History.</p>
                                        </div>
                                        <div class="csv-toolbar">
                                            <button type="button" class="btn-csv" onclick="exportDefectsToCSV()" title="Download CSV report">
                                                <i class="fa-solid fa-download" style="color:#0263b3;"></i> Export CSV
                                            </button>
                                            <button type="button" class="btn-csv" onclick="openCsvImportModal()" title="Upload CSV records">
                                                <i class="fa-solid fa-file-import" style="color:#10b981;"></i> Import CSV
                                            </button>
                                        </div>
                                    </div>

                                    <div class="task-filter-grid">
                                        <div>
                                            <label style="font-size:0.62rem; color:#94a3b8; font-weight:700;">TOWN COUNCIL</label>
                                            <select class="figma-input" style="padding:5px 8px; font-size:0.72rem;">
                                                <option>Woodlands (SBTC)</option>
                                            </select>
                                        </div>
                                        <div>
                                            <label style="font-size:0.62rem; color:#94a3b8; font-weight:700;">LIFT COMPANY</label>
                                            <select class="figma-input" id="managerFilterCompany" onchange="filterManagerTasksByCompany(this.value)" style="padding:5px 8px; font-size:0.72rem;">
                                                <option value="all">All companies</option>
                                                <option value="Mitsubishi">Mitsubishi</option>
                                                <option value="Fujitec">Fujitec</option>
                                                <option value="Schindler">Schindler</option>
                                                <option value="KONE">KONE</option>
                                            </select>
                                        </div>
                                        <div>
                                            <label style="font-size:0.62rem; color:#94a3b8; font-weight:700;">BLOCK / LIFT</label>
                                            <select class="figma-input" style="padding:5px 8px; font-size:0.72rem;">
                                                <option>All</option>
                                                <option>556/A</option>
                                                <option>556/B</option>
                                                <option>557/B</option>
                                                <option>559/A</option>
                                            </select>
                                        </div>
                                        <div>
                                            <label style="font-size:0.62rem; color:#94a3b8; font-weight:700;">ADDRESS</label>
                                            <input type="text" class="figma-input" style="padding:5px 8px; font-size:0.72rem;" value="Woodlands St 53" readonly>
                                        </div>
                                        <div>
                                            <label style="font-size:0.62rem; color:#94a3b8; font-weight:700;">RECTIFICATION DUE</label>
                                            <input type="text" class="figma-input" style="padding:5px 8px; font-size:0.72rem;" value="By 11/04/2026" readonly>
                                        </div>
                                    </div>
                                </div>

                                <!-- Sub-tabs: All Active (5), Awaiting Sign-off (1), History (2) -->
                                <div class="task-tab-pills">
                                    <button type="button" class="task-tab-pill active" id="tabBtnActive" onclick="filterManagerTasks('all')">All Active (<span id="countActivePill">5</span>)</button>
                                    <button type="button" class="task-tab-pill" id="tabBtnAwaiting" onclick="filterManagerTasks('awaiting')">Awaiting Sign-off (<span id="countAwaitingPill">1</span>)</button>
                                    <button type="button" class="task-tab-pill" id="tabBtnHistory" onclick="filterManagerTasks('history')">History (<span id="countHistoryPill">2</span>)</button>
                                </div>

                                <!-- TAB 1: ALL ACTIVE DEFECTS (ALL 5 ARE CLICKABLE & EXPANDABLE) -->
                                <div id="panelActiveDefects">
                                    <!-- Defect 1: Minor (Cleanliness) - CAN OPEN FOR SIGN OFF -->
                                    <div class="defect-row-card" id="cardDefect1">
                                        <div class="defect-row-top clickable-defect-header" onclick="toggleDefectDrawer('drawerDefect1')">
                                            <div class="defect-row-title">
                                                <h4><i class="fa-solid fa-chevron-down" style="font-size:0.7rem; color:#0263b3; margin-right:4px;"></i> (1) Motor room cleanliness - any debris?</h4>
                                                <p>D-0412 • (A) Motor Room • 556/A Woodlands St 53 (Mitsubishi)</p>
                                            </div>
                                            <span class="severity-pill minor">● Minor</span>
                                        </div>
                                        <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.7rem; color:#64748b;">
                                            <span>Spot-check: 28/03/2026</span>
                                            <span style="color:#2563eb; font-weight:700;">Due: 11/04/2026 (4 days left)</span>
                                            <span class="status-badge" style="background:#fef3c7; color:#b45309;">Pending Rectification</span>
                                        </div>

                                        <!-- Minor Drawer for Sign-off -->
                                        <div id="drawerDefect1" class="defect-details-drawer" style="display:none;">
                                            <div style="background:#f8fafc; padding:8px; border-radius:6px;">
                                                <strong>Contractor Note:</strong> Loose debris swept and cleared from machine bed. Minor task completed.
                                            </div>
                                            <div class="alert-box success" style="margin:4px 0; padding:6px 10px;">
                                                <i class="fa-solid fa-circle-check"></i>
                                                <span>Minor Defect: No photo upload required. Fast-track sign-off eligible.</span>
                                            </div>
                                            <div class="rectification-progress-bar">
                                                <div class="progress-step-item">
                                                    <div class="step-dot done"></div>
                                                    <span>Flagged<br>28/03</span>
                                                </div>
                                                <div class="progress-step-item">
                                                    <div class="step-dot done"></div>
                                                    <span>Dispatched<br>28/03</span>
                                                </div>
                                                <div class="progress-step-item">
                                                    <div class="step-dot done"></div>
                                                    <span>Rectified<br>02/04</span>
                                                </div>
                                                <div class="progress-step-item">
                                                    <div class="step-dot active"></div>
                                                    <span>Sign-off<br>Waiting</span>
                                                </div>
                                                <div class="progress-step-item">
                                                    <div class="step-dot"></div>
                                                    <span>History</span>
                                                </div>
                                            </div>
                                            <div style="display:flex; gap:8px; justify-content:flex-end; margin-top:6px;">
                                                <button type="button" class="btn-secondary-outline" style="color:#ef4444; border-color:#fca5a5; width:auto; font-size:0.7rem;" onclick="showScreen('task-rework')">
                                                    Send Back for Rework
                                                </button>
                                                <button type="button" class="btn-primary-blue" style="width:auto; font-size:0.7rem;" onclick="signOffDefect('D-0412', 'cardDefect1', '(1) Motor room cleanliness')">
                                                    <i class="fa-solid fa-check"></i> Sign Off (Minor)
                                                </button>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Defect 2: Major (Wire Ropes) -->
                                    <div class="defect-row-card" id="cardDefect2">
                                        <div class="defect-row-top clickable-defect-header" onclick="toggleDefectDrawer('drawerDefect2')">
                                            <div class="defect-row-title">
                                                <h4><i class="fa-solid fa-chevron-down" style="font-size:0.7rem; color:#0263b3; margin-right:4px;"></i> (5) Wire ropes & sheaves - any wear or red dust?</h4>
                                                <p>D-0413 • (A) Motor Room • 556/B Woodlands St 53 (Mitsubishi)</p>
                                            </div>
                                            <span class="severity-pill major">● Major</span>
                                        </div>
                                        <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.7rem; color:#64748b;">
                                            <span>Spot-check: 28/03/2026</span>
                                            <span style="color:#d97706; font-weight:700;">In Progress (3 days left)</span>
                                            <span class="status-badge" style="background:#eff6ff; color:#1d4ed8;">In Progress</span>
                                        </div>

                                        <div id="drawerDefect2" class="defect-details-drawer" style="display:none;">
                                            <div><strong>Contractor Note:</strong> Sheaves cleaned and governor ropes re-lubricated. Photo evidence attached.</div>
                                            <div>
                                                <strong>Photo evidence:</strong>
                                                <span class="photo-thumb-chip"><i class="fa-solid fa-image"></i> wire_rope1.jpg (74 KB)</span>
                                                <span class="photo-thumb-chip"><i class="fa-solid fa-image"></i> governor_sheave.jpg (82 KB)</span>
                                            </div>
                                            <div class="rectification-progress-bar">
                                                <div class="progress-step-item">
                                                    <div class="step-dot done"></div>
                                                    <span>Flagged<br>28/03</span>
                                                </div>
                                                <div class="progress-step-item">
                                                    <div class="step-dot done"></div>
                                                    <span>Sent<br>28/03</span>
                                                </div>
                                                <div class="progress-step-item">
                                                    <div class="step-dot active"></div>
                                                    <span>Rectifying<br>In Progress</span>
                                                </div>
                                                <div class="progress-step-item">
                                                    <div class="step-dot"></div>
                                                    <span>Sign-off</span>
                                                </div>
                                                <div class="progress-step-item">
                                                    <div class="step-dot"></div>
                                                    <span>History</span>
                                                </div>
                                            </div>
                                            <div style="display:flex; gap:8px; justify-content:flex-end; margin-top:6px;">
                                                <button type="button" class="btn-primary-blue" style="width:auto; font-size:0.7rem;" onclick="signOffDefect('D-0413', 'cardDefect2', '(5) Wire ropes & sheaves')">
                                                    <i class="fa-solid fa-check"></i> Endorse & Sign Off
                                                </button>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Defect 3: Major Overdue (Controller Contactors) -->
                                    <div class="defect-row-card" id="cardDefect3">
                                        <div class="defect-row-top clickable-defect-header" onclick="toggleDefectDrawer('drawerDefect3')">
                                            <div class="defect-row-title">
                                                <h4><i class="fa-solid fa-chevron-down" style="font-size:0.7rem; color:#ef4444; margin-right:4px;"></i> (3) Controller contactors & relays - any humming?</h4>
                                                <p>D-0414 • (A) Motor Room • 557/B Woodlands St 53 (Schindler)</p>
                                            </div>
                                            <span class="severity-pill major">● Major</span>
                                        </div>
                                        <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.7rem;">
                                            <span style="color:#64748b;">Spot-check: 28/03/2026</span>
                                            <span style="color:#ef4444; font-weight:700;">Due: 04/04/2026 (3 days overdue)</span>
                                            <span class="status-badge" style="background:#fee2e2; color:#b91c1c;">Overdue</span>
                                        </div>

                                        <div id="drawerDefect3" class="defect-details-drawer" style="display:none;">
                                            <div class="alert-box danger" style="padding:6px 10px; margin:4px 0;">
                                                <i class="fa-solid fa-triangle-exclamation"></i>
                                                <span>Overdue 3 days! Schindler Contractor supervisor notified for urgent coil replacement.</span>
                                            </div>
                                            <div><strong>Rectification Action:</strong> Replacement contactor coil scheduled for immediate delivery.</div>
                                            <div style="display:flex; gap:8px; justify-content:flex-end; margin-top:6px;">
                                                <button type="button" class="btn-primary-blue" style="background:#ef4444; width:auto; font-size:0.7rem;" onclick="showToast('Expedite notice dispatched to Schindler!')">
                                                    <i class="fa-solid fa-bell"></i> Send Urgent Reminder
                                                </button>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Defect 4: Minor (Bearings) - CAN OPEN FOR SIGN OFF -->
                                    <div class="defect-row-card" id="cardDefect4">
                                        <div class="defect-row-top clickable-defect-header" onclick="toggleDefectDrawer('drawerDefect4')">
                                            <div class="defect-row-title">
                                                <h4><i class="fa-solid fa-chevron-down" style="font-size:0.7rem; color:#0263b3; margin-right:4px;"></i> (4) Bearings - any abnormal noise?</h4>
                                                <p>D-0415 • (A) Motor Room • 558/A Woodlands St 53 (KONE)</p>
                                            </div>
                                            <span class="severity-pill minor">● Minor</span>
                                        </div>
                                        <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.7rem; color:#64748b;">
                                            <span>Spot-check: 28/03/2026</span>
                                            <span style="color:#2563eb; font-weight:700;">Due: 11/04/2026 in 4 days</span>
                                            <span class="status-badge" style="background:#fef3c7; color:#b45309;">Pending Rectification</span>
                                        </div>

                                        <div id="drawerDefect4" class="defect-details-drawer" style="display:none;">
                                            <div style="background:#f8fafc; padding:8px; border-radius:6px;">
                                                <strong>Contractor Note:</strong> Bearing lubricated and acoustic sensor test within normal dB threshold.
                                            </div>
                                            <div class="alert-box success" style="margin:4px 0; padding:6px 10px;">
                                                <i class="fa-solid fa-circle-check"></i>
                                                <span>Minor Defect: Fast-track sign-off eligible.</span>
                                            </div>
                                            <div style="display:flex; gap:8px; justify-content:flex-end; margin-top:6px;">
                                                <button type="button" class="btn-primary-blue" style="width:auto; font-size:0.7rem;" onclick="signOffDefect('D-0415', 'cardDefect4', '(4) Bearings - abnormal noise')">
                                                    <i class="fa-solid fa-check"></i> Sign Off (Minor)
                                                </button>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Defect 5: Major Awaiting Sign-off (Fujitec ARD & EBOPS) -->
                                    <div class="defect-row-card" id="cardDefect5" style="border-color:#bfdbfe; background:#f0f7ff;">
                                        <div class="defect-row-top clickable-defect-header" onclick="toggleDefectDrawer('drawerDefect5')">
                                            <div class="defect-row-title">
                                                <h4><i class="fa-solid fa-chevron-down" style="font-size:0.7rem; color:#0263b3; margin-right:4px;"></i> (9) ARD & EBOPS - functioning? Replacement date?</h4>
                                                <p>D-0417 • (A) Motor Room • 559/A Woodlands St 54 (Fujitec)</p>
                                            </div>
                                            <span class="severity-pill major">● Major</span>
                                        </div>
                                        <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.7rem; color:#64748b;">
                                            <span>Spot-check: 28/03/2026</span>
                                            <span style="color:#10b981; font-weight:700;">Rectified: 03/04/2026</span>
                                            <span class="status-badge" style="background:#dbeafe; color:#1e40af;">Awaiting Sign-off</span>
                                        </div>

                                        <div id="drawerDefect5" class="defect-details-drawer">
                                            <div><strong>Lift company note:</strong> ARD & EBOPS tested and functioning. Battery pack replaced.</div>
                                            <div>
                                                <strong>Photo evidence:</strong>
                                                <span class="photo-thumb-chip"><i class="fa-solid fa-image"></i> ard_test.jpg</span>
                                                <span class="photo-thumb-chip"><i class="fa-solid fa-image"></i> battery_new.jpg</span>
                                                <span style="color:#ef4444; font-size:0.65rem; font-weight:700; margin-left:4px;">Required for Major</span>
                                            </div>
                                            <div style="display:flex; justify-content:space-between; font-size:0.7rem;">
                                                <span>Rectified on: <strong>03/04/2026</strong></span>
                                                <span>Next replacement: <strong>15/11/2028</strong></span>
                                            </div>

                                            <div class="rectification-progress-bar">
                                                <div class="progress-step-item">
                                                    <div class="step-dot done"></div>
                                                    <span>Defect flagged<br>28/03/2026</span>
                                                </div>
                                                <div class="progress-step-item">
                                                    <div class="step-dot done"></div>
                                                    <span>Sent to Fujitec<br>28/03/2026</span>
                                                </div>
                                                <div class="progress-step-item">
                                                    <div class="step-dot done"></div>
                                                    <span>Rectified by Fujitec<br>03/04/2026</span>
                                                </div>
                                                <div class="progress-step-item">
                                                    <div class="step-dot active"></div>
                                                    <span>Sign-off<br>Waiting for you</span>
                                                </div>
                                                <div class="progress-step-item">
                                                    <div class="step-dot"></div>
                                                    <span>Moved to History<br>After sign-off</span>
                                                </div>
                                            </div>

                                            <div style="display:flex; gap:8px; justify-content:flex-end; margin-top:8px;">
                                                <button type="button" class="btn-secondary-outline" style="color:#ef4444; border-color:#fca5a5; width:auto;" onclick="showScreen('task-rework')">
                                                    Send Back for Rework
                                                </button>
                                                <button type="button" class="btn-primary-blue" style="width:auto;" onclick="signOffDefect('D-0417', 'cardDefect5', '(9) ARD & EBOPS')">
                                                    <i class="fa-solid fa-check"></i> Sign Off
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- TAB 2: AWAITING SIGN-OFF QUEUE (HOLDS DISTINCT INFORMATION) -->
                                <div id="panelAwaitingDefects" style="display:none;">
                                    <div class="alert-box" style="background:#eff6ff; border-color:#bfdbfe; color:#1e40af; margin-bottom:10px;">
                                        <i class="fa-solid fa-circle-info"></i>
                                        <span>Showing rectifications submitted by contractors that require your final endorsement before closing.</span>
                                    </div>

                                    <div class="defect-row-card" style="border-left:4px solid #0263b3; background:#ffffff;">
                                        <div class="defect-row-top">
                                            <div>
                                                <h4>(9) ARD & EBOPS - functioning? Replacement date?</h4>
                                                <p>D-0417 • Blk 559/A Woodlands St 54 • Fujitec Singapore</p>
                                            </div>
                                            <span class="status-badge" style="background:#dbeafe; color:#1e40af;">Awaiting Endorsement</span>
                                        </div>
                                        <div style="font-size:0.72rem; color:#475569; margin:6px 0;">
                                            Submitted by: Fujitec Senior Technician Tan • Rectified 03/04/2026 • Evidence photos attached (2 photos).
                                        </div>
                                        <div style="display:flex; gap:8px; justify-content:flex-end; margin-top:8px;">
                                            <button type="button" class="btn-secondary-outline" style="color:#ef4444; border-color:#fca5a5; width:auto; font-size:0.72rem;" onclick="showScreen('task-rework')">
                                                Send Back for Rework
                                            </button>
                                            <button type="button" class="btn-primary-blue" style="width:auto; font-size:0.72rem;" onclick="signOffDefect('D-0417', 'cardDefect5', '(9) ARD & EBOPS')">
                                                <i class="fa-solid fa-check"></i> Endorse & Close Task
                                            </button>
                                        </div>
                                    </div>
                                </div>

                                <!-- TAB 3: HISTORY (HOLDS DISTINCT INFORMATION & REOPEN ACTION) -->
                                <div id="panelHistoryDefects" style="display:none;">
                                    <div class="alert-box success" style="margin-bottom:10px;">
                                        <i class="fa-solid fa-box-archive"></i>
                                        <span>Past job scope: signed-off defects. Reopen any defect that needs to be rectified again.</span>
                                    </div>

                                    <div class="defect-row-card">
                                        <div class="defect-row-top">
                                            <div>
                                                <h4>(2) Cleanliness of traction machine - any leakage?</h4>
                                                <p>D-0391 • Blk 556/A Woodlands St 53 • Mitsubishi Elevator</p>
                                            </div>
                                            <span class="status-badge" style="background:#dcfce7; color:#166534;">Signed Off</span>
                                        </div>
                                        <p style="font-size:0.7rem; color:#64748b; margin:4px 0;">Rectified on 02/04/2026 • Signed off by: A. Lee (Officer-in-charge)</p>
                                        <button type="button" class="btn-secondary-outline" style="width:auto; font-size:0.68rem; color:#ef4444; border-color:#fca5a5; margin-top:4px;" onclick="openReopenModal('D-0391 - Traction Machine Oil Leakage')">
                                            <i class="fa-solid fa-rotate-left"></i> Reopen Defect
                                        </button>
                                    </div>

                                    <div class="defect-row-card">
                                        <div class="defect-row-top">
                                            <div>
                                                <h4>(3) Landing door lock adjustment - any noise?</h4>
                                                <p>D-0388 • Blk 554/B Woodlands St 53 • Schindler Lifts</p>
                                            </div>
                                            <span class="status-badge" style="background:#dcfce7; color:#166534;">Signed Off</span>
                                        </div>
                                        <p style="font-size:0.7rem; color:#64748b; margin:4px 0;">Rectified on 14/03/2026 • Signed off by: Wee Boon (Inspector)</p>
                                        <button type="button" class="btn-secondary-outline" style="width:auto; font-size:0.68rem; color:#ef4444; border-color:#fca5a5; margin-top:4px;" onclick="openReopenModal('D-0388 - Landing Door Lock')">
                                            <i class="fa-solid fa-rotate-left"></i> Reopen Defect
                                        </button>
                                    </div>
                                </div>
                            </div>

                            <!-- Subview 3: Resident Reports Received -->
                            <div id="manager-sub-resident-reports" class="subview-container">
                                <div class="role-welcome-banner">
                                    <h1>Resident Lift Complaints & Reports</h1>
                                    <p>Tickets submitted by residents of Sembawang Town Council blocks.</p>
                                </div>

                                <div class="defect-row-card">
                                    <div class="defect-row-top">
                                        <div class="defect-row-title">
                                            <h4>Loud humming noise between 7th & 9th floor</h4>
                                            <p>Ticket #R-104 • Blk 554 Lift A • Reported by Daniel Tan (#09-241)</p>
                                        </div>
                                        <span class="status-badge" style="background:#fef3c7; color:#d97706;">Investigating</span>
                                    </div>
                                    <p style="font-size:0.72rem; color:#475569; margin:4px 0;">"Rattling sound when lift travels up past floor 8. Started 2 days ago."</p>
                                    <div style="display:flex; gap:8px; margin-top:6px;">
                                        <button type="button" class="btn-primary-blue" style="width:auto; padding:4px 10px; font-size:0.7rem;" onclick="showToast('Dispatched to Mitsubishi Technician')">Dispatch Contractor</button>
                                    </div>
                                </div>

                                <div class="defect-row-card">
                                    <div class="defect-row-top">
                                        <div class="defect-row-title">
                                            <h4>Door sensor slow to reopen when obstructed</h4>
                                            <p>Ticket #R-102 • Blk 556 Lift B • Reported by Sarah Ong</p>
                                        </div>
                                        <span class="status-badge" style="background:#dcfce7; color:#166534;">Resolved</span>
                                    </div>
                                    <p style="font-size:0.72rem; color:#475569; margin:4px 0;">Safety curtain realigned during routine maintenance.</p>
                                </div>
                            </div>

                            <!-- Subview 4: Reports & SLA Compliance -->
                            <div id="manager-sub-reports" class="subview-container">
                                <div class="role-welcome-banner">
                                    <h1>Estate SLA & Contractor Performance</h1>
                                    <p>2-Week Defect Rectification Turnaround (14-day SLA benchmark).</p>
                                </div>

                                <div class="portal-selection-card" style="text-align:left; align-items:stretch; padding:16px;">
                                    <h3 style="font-size:0.95rem; font-weight:800; color:#0f2b48;">Monthly Servicing Summary (March 2026)</h3>
                                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:10px 0;">
                                        <div style="background:#f8fafc; padding:10px; border-radius:8px;">
                                            <div style="font-size:0.65rem; color:#64748b;">TOTAL SPOT-CHECKS</div>
                                            <div style="font-size:1.3rem; font-weight:800; color:#0263b3;">124 Lifts</div>
                                        </div>
                                        <div style="background:#f8fafc; padding:10px; border-radius:8px;">
                                            <div style="font-size:0.65rem; color:#64748b;">14-DAY RECTIFICATION SLA</div>
                                            <div style="font-size:1.3rem; font-weight:800; color:#10b981;">96.4% Met</div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Subview 5: Notifications & Schedule -->
                            <div id="manager-sub-schedule" class="subview-container">
                                <div class="role-welcome-banner">
                                    <h1>Monthly Inspection Schedule</h1>
                                    <p>Plan upcoming spot-checks following routine lift servicing.</p>
                                </div>

                                <div class="defect-row-card">
                                    <h4>Blk 554 Lift A & B - Next Spot-Check</h4>
                                    <p style="font-size:0.72rem; color:#64748b;">Scheduled for 28/04/2026 • Inspector Wee Boon assigned</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- ============================================================== -->
                <!-- ROLE 2: LIFT CONTRACTOR DASHBOARD (CHARTS + MASTER TABLE)      -->
                <!-- ============================================================== -->
                <div id="view-role-contractor" class="screen-view">
                    <div class="dashboard-layout-wrap">
                        <aside class="role-desktop-sidebar contractor">
                            <div>
                                <div class="sidebar-group-title">Contractor</div>
                                <ul class="sidebar-nav-list">
                                    <li class="sidebar-nav-item">
                                        <button type="button" class="active" onclick="clickRoleTab('contractor', 0, 'home', 'Home')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-chart-pie"></i> Operations</span>
                                        </button>
                                    </li>
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="clickRoleTab('contractor', 1, 'rectify', 'Active Tasks')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-wrench"></i> Active Tasks</span>
                                            <span class="sidebar-item-badge">4</span>
                                        </button>
                                    </li>
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="clickRoleTab('contractor', 2, 'awaiting', 'Awaiting Sign-off')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-clock-rotate-left"></i> Awaiting Sign-off</span>
                                            <span class="sidebar-item-badge">1</span>
                                        </button>
                                    </li>
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="clickRoleTab('contractor', 3, 'history', 'Past Defects')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-box-archive"></i> Past Defects</span>
                                        </button>
                                    </li>
                                </ul>
                            </div>
                            <div>
                                <div class="sidebar-group-title">Contacts</div>
                                <ul class="sidebar-nav-list">
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="showToast('Contractor Control Centre: 6475 1188')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-phone"></i> Emergency Contact</span>
                                        </button>
                                    </li>
                                </ul>
                            </div>
                        </aside>

                        <div class="dashboard-main-panel">
                            <!-- Subview 1: Contractor Home / Operations Dashboard with Charts -->
                            <div id="contractor-sub-home" class="subview-container active">
                                <div class="role-welcome-banner">
                                    <h1>Contractor Operations Dashboard</h1>
                                    <p>Mitsubishi Elevator Singapore Pte Ltd • Service & Maintenance Division</p>
                                </div>

                                <!-- Operational Summary Cards -->
                                <div class="contractor-summary-grid">
                                    <div class="contractor-kpi-card">
                                        <div class="kpi-label">Total Active Blocks</div>
                                        <div class="kpi-value">48</div>
                                        <div class="kpi-sub">Across 4 Town Council Divisions</div>
                                    </div>
                                    <div class="contractor-kpi-card">
                                        <div class="kpi-label">Overall Lift Uptime</div>
                                        <div class="kpi-value" style="color:#10b981;">99.4%</div>
                                        <div class="kpi-sub">● Above 99.0% SLA Target</div>
                                    </div>
                                    <div class="contractor-kpi-card">
                                        <div class="kpi-label">Pending Sign-offs</div>
                                        <div class="kpi-value" style="color:#d97706;">3</div>
                                        <div class="kpi-sub">Awaiting joint endorsement</div>
                                    </div>
                                    <div class="contractor-kpi-card">
                                        <div class="kpi-label">Critical Active Faults</div>
                                        <div class="kpi-value" style="color:#ef4444;">2</div>
                                        <div class="kpi-sub">Immediate attention required</div>
                                    </div>
                                </div>

                                <!-- Quick Actions Strip -->
                                <div class="quick-action-strip">
                                    <button type="button" class="btn-primary-blue" style="background:#d97706; width:auto;" onclick="openAssignTechModal()">
                                        <i class="fa-solid fa-user-plus"></i> Assign Technician
                                    </button>
                                    <button type="button" class="btn-secondary-outline" style="width:auto;" onclick="openBroadcastModal()">
                                        <i class="fa-solid fa-bullhorn"></i> Broadcast Notice to Residents
                                    </button>
                                </div>

                                <!-- Interactive Charts Row -->
                                <div class="charts-row-grid">
                                    <!-- Chart 1: HDB Zones Distribution -->
                                    <div class="interactive-chart-card">
                                        <div class="chart-header">
                                            <h3>Fault Distribution by HDB Zones</h3>
                                            <span style="font-size:0.65rem; color:#64748b;">Live Data</span>
                                        </div>
                                        <div class="bar-chart-list">
                                            <div class="bar-item">
                                                <div class="bar-item-meta">
                                                    <span>Woodlands North</span>
                                                    <span>35% (7 faults)</span>
                                                </div>
                                                <div class="bar-track">
                                                    <div class="bar-fill" style="width:35%; background:#d97706;"></div>
                                                </div>
                                            </div>
                                            <div class="bar-item">
                                                <div class="bar-item-meta">
                                                    <span>Woodlands East</span>
                                                    <span>28% (5 faults)</span>
                                                </div>
                                                <div class="bar-track">
                                                    <div class="bar-fill" style="width:28%; background:#f59e0b;"></div>
                                                </div>
                                            </div>
                                            <div class="bar-item">
                                                <div class="bar-item-meta">
                                                    <span>Marsiling Zone</span>
                                                    <span>22% (4 faults)</span>
                                                </div>
                                                <div class="bar-track">
                                                    <div class="bar-fill" style="width:22%; background:#3b82f6;"></div>
                                                </div>
                                            </div>
                                            <div class="bar-item">
                                                <div class="bar-item-meta">
                                                    <span>Woodgrove Division</span>
                                                    <span>15% (3 faults)</span>
                                                </div>
                                                <div class="bar-track">
                                                    <div class="bar-fill" style="width:15%; background:#10b981;"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Chart 2: Severity Levels Breakdown -->
                                    <div class="interactive-chart-card">
                                        <div class="chart-header">
                                            <h3>Defect Severity Breakdown</h3>
                                            <span style="font-size:0.65rem; color:#64748b;">Current Active</span>
                                        </div>
                                        <div style="display:flex; align-items:center; justify-content:space-around; height:120px;">
                                            <div style="text-align:center;">
                                                <div style="font-size:1.8rem; font-weight:800; color:#f59e0b;">60%</div>
                                                <div style="font-size:0.68rem; color:#64748b; font-weight:700;">Minor Issues</div>
                                                <span style="font-size:0.62rem; color:#94a3b8;">No photo required</span>
                                            </div>
                                            <div style="width:1px; height:60px; background:#e2e8f0;"></div>
                                            <div style="text-align:center;">
                                                <div style="font-size:1.8rem; font-weight:800; color:#ef4444;">40%</div>
                                                <div style="font-size:0.68rem; color:#64748b; font-weight:700;">Major Issues</div>
                                                <span style="font-size:0.62rem; color:#94a3b8;">Photo (&lt;100KB)</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Filterable Master Task Table with Drill-down -->
                                <div class="task-header-block">
                                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
                                        <h3 style="font-size:0.95rem; font-weight:800; color:#0f2b48;">Master Task Management & Drill-Down</h3>
                                        <input type="text" id="contractorTaskSearch" placeholder="Search tasks, blocks..." oninput="filterContractorMasterTable()" class="figma-input" style="width:180px; padding:4px 8px; font-size:0.7rem;">
                                    </div>

                                    <div style="display:flex; gap:8px; margin-bottom:8px;">
                                        <select class="figma-input" id="contractorZoneSelect" onchange="filterContractorMasterTable()" style="padding:4px 8px; font-size:0.7rem;">
                                            <option value="all">All HDB Zones</option>
                                            <option value="Woodlands North">Woodlands North</option>
                                            <option value="Woodlands East">Woodlands East</option>
                                            <option value="Marsiling">Marsiling</option>
                                            <option value="Woodgrove">Woodgrove</option>
                                        </select>
                                        <select class="figma-input" id="contractorSeveritySelect" onchange="filterContractorMasterTable()" style="padding:4px 8px; font-size:0.7rem;">
                                            <option value="all">All Severities</option>
                                            <option value="Minor">Minor</option>
                                            <option value="Major">Major</option>
                                        </select>
                                    </div>

                                    <div id="contractorMasterTableList">
                                        <div class="defect-row-card contractor-task-item" data-zone="Woodlands North" data-severity="Minor" onclick="toggleDefectDrawer('contractorDrill1')">
                                            <div class="defect-row-top">
                                                <div>
                                                    <h4 style="font-size:0.78rem;">Blk 556/A • (1) Motor room cleanliness</h4>
                                                    <span style="font-size:0.65rem; color:#64748b;">Zone: Woodlands North • Assigned to: Ah Seng</span>
                                                </div>
                                                <span class="severity-pill minor">Minor</span>
                                            </div>
                                            <div id="contractorDrill1" style="display:none; margin-top:8px; padding-top:6px; border-top:1px dashed #cbd5e1; font-size:0.7rem;">
                                                <p><strong>Work scope:</strong> Sweep and bag loose dust near traction machine bed.</p>
                                                <p><strong>Due:</strong> 11/04/2026 • <strong>SLA:</strong> 4 days remaining</p>
                                            </div>
                                        </div>

                                        <div class="defect-row-card contractor-task-item" data-zone="Woodlands North" data-severity="Major" onclick="toggleDefectDrawer('contractorDrill2')">
                                            <div class="defect-row-top">
                                                <div>
                                                    <h4 style="font-size:0.78rem;">Blk 556/B • (5) Wire ropes & sheaves red dust</h4>
                                                    <span style="font-size:0.65rem; color:#64748b;">Zone: Woodlands North • Assigned to: Kumar</span>
                                                </div>
                                                <span class="severity-pill major">Major</span>
                                            </div>
                                            <div id="contractorDrill2" style="display:none; margin-top:8px; padding-top:6px; border-top:1px dashed #cbd5e1; font-size:0.7rem;">
                                                <p><strong>Work scope:</strong> Degrease main hoisting ropes and lubricate with approved compound. Attach photo.</p>
                                                <p><strong>Due:</strong> 10/04/2026 • <strong>SLA:</strong> 3 days remaining</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Subview 2: Active Tasks / Rectification Detail -->
                            <div id="contractor-sub-rectify" class="subview-container">
                                <div class="task-header-block">
                                    <h2 style="font-size:1.1rem; font-weight:800; color:#0f2b48;">Blk 556/A & 556/B Woodlands St 53</h2>
                                    <p style="font-size:0.72rem; color:#64748b;">Complete repairs flagged during spot-check on 28/03/2026:</p>
                                </div>

                                <div class="defect-row-card">
                                    <div class="defect-row-top">
                                        <div>
                                            <h4>(1) Motor room cleanliness - any debris?</h4>
                                            <p>Block/Lift: 556/A • Mitsubishi • Spot-check: 28/03/2026 • Rectify by: 11/04/2026</p>
                                        </div>
                                        <span class="severity-pill minor">Minor</span>
                                    </div>
                                    <p style="font-size:0.72rem; color:#475569; margin:4px 0;"><strong>Remarks:</strong> Dust and loose debris around the traction machine base.</p>
                                    <div class="alert-box" style="background:#f1f5f9; border-color:#e2e8f0; color:#64748b; margin-top:6px;">
                                        <i class="fa-solid fa-circle-info"></i>
                                        <span>No photo required for minor issue. Ready to submit directly.</span>
                                    </div>
                                </div>

                                <div class="defect-row-card" style="border-color:#fde68a;">
                                    <div class="defect-row-top">
                                        <div>
                                            <h4>(5) Wire ropes & sheaves - any wear or red dust?</h4>
                                            <p>Block/Lift: 556/B • Mitsubishi • Spot-check: 28/03/2026 • Rectify by: 10/04/2026</p>
                                        </div>
                                        <span class="severity-pill major">Major</span>
                                    </div>
                                    <p style="font-size:0.72rem; color:#475569; margin:4px 0;"><strong>Remarks:</strong> Red dust found on main ropes; wear visible on governor sheaves.</p>
                                    
                                    <div class="photo-uploader-box" onclick="showToast('Photo evidence attached: wire_rope1.jpg (74 KB) - under 100KB limit')">
                                        <i class="fa-solid fa-cloud-arrow-up" style="font-size:1.5rem; color:#0263b3; margin-bottom:4px;"></i>
                                        <div><strong>Drop photos here or Browse Files</strong></div>
                                        <div style="font-size:0.65rem; color:#64748b;">JPG or PNG up to 5 photos • Strict &lt;100KB limit per photo</div>
                                    </div>

                                    <div class="photo-thumbnails-row">
                                        <span class="photo-thumb-chip"><i class="fa-solid fa-image"></i> wire_rope1.jpg (74 KB)</span>
                                        <span class="photo-thumb-chip"><i class="fa-solid fa-image"></i> governor_sheave.jpg (82 KB)</span>
                                    </div>
                                </div>

                                <div class="signature-card">
                                    <div style="display:flex; justify-content:space-between; font-size:0.74rem; font-weight:700; margin-bottom:4px;">
                                        <span><i class="fa-solid fa-signature"></i> Technician Signature (Rectified By)</span>
                                        <button type="button" style="background:none; border:none; color:#ef4444; font-size:0.7rem; cursor:pointer;" id="btnClearTechSign">Clear</button>
                                    </div>
                                    <canvas id="canvasTechSign" class="signature-canvas" width="380" height="85"></canvas>
                                </div>

                                <button type="button" class="btn-primary-blue" style="background:#d97706;" onclick="showToast('Submitted for Officer Sign-off!'); clickRoleTab('contractor', 2, 'awaiting', 'Awaiting Sign-off');">
                                    <i class="fa-solid fa-paper-plane"></i> Submit for Sign-off
                                </button>
                            </div>

                            <!-- Subview 3: Awaiting Sign-off -->
                            <div id="contractor-sub-awaiting" class="subview-container">
                                <div class="role-welcome-banner">
                                    <h1>Awaiting Sign-off</h1>
                                    <p>Jobs submitted to Estate Manager awaiting joint inspection endorsement.</p>
                                </div>

                                <div class="defect-row-card" style="background:#f0fdf4; border-color:#bbf7d0;">
                                    <span class="status-badge" style="background:#dcfce7; color:#15803d;">Submitted</span>
                                    <h4 style="margin:4px 0;">Blk 554 Lift A - 4 Defects Cleared</h4>
                                    <p style="font-size:0.72rem; color:#166534;">Waiting for LMS Inspector Wee Boon joint endorsement.</p>
                                </div>
                            </div>

                            <!-- Subview 4: History / Past Defects -->
                            <div id="contractor-sub-history" class="subview-container">
                                <div class="role-welcome-banner">
                                    <h1>Past Job Scope (Signed-Off Defects)</h1>
                                    <p>Signed-off defects. Reopen any defect that needs to be rectified again.</p>
                                </div>

                                <div class="defect-row-card">
                                    <div class="defect-row-top">
                                        <div>
                                            <h4>(2) Cleanliness of traction machine - any leakage?</h4>
                                            <p>556/A • Mitsubishi • Spot-check: 14/03/2026 • Rectified on: 02/04/2026</p>
                                        </div>
                                        <span class="status-badge" style="background:#dcfce7; color:#166534;">Signed Off</span>
                                    </div>
                                    <p style="font-size:0.72rem; color:#64748b;">Signed off by: A. Lee • Officer-in-charge</p>
                                    <button type="button" class="btn-secondary-outline" style="width:auto; margin-top:8px; font-size:0.7rem; color:#ef4444; border-color:#fca5a5;" onclick="openReopenModal('D-0391 - Traction Machine Oil Leakage')">
                                        Reopen Defect
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- ============================================================== -->
                <!-- ROLE 3: EMS INSPECTOR DASHBOARD (SENT-BACK QUEUE + FAST FIELD) -->
                <!-- ============================================================== -->
                <div id="view-role-inspector" class="screen-view">
                    <div class="dashboard-layout-wrap">
                        <aside class="role-desktop-sidebar inspector">
                            <div>
                                <div class="sidebar-group-title">EMS Inspector</div>
                                <ul class="sidebar-nav-list">
                                    <li class="sidebar-nav-item">
                                        <button type="button" class="active" onclick="clickRoleTab('inspector', 0, 'home', 'Home')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-house"></i> Field Home</span>
                                        </button>
                                    </li>
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="clickRoleTab('inspector', 1, 'checklist', 'New Inspection')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-clipboard-check"></i> Form 12b Check</span>
                                        </button>
                                    </li>
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="clickRoleTab('inspector', 2, 'queue', 'My Inspections')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-list-check"></i> Daily Queue</span>
                                            <span class="sidebar-item-badge">3</span>
                                        </button>
                                    </li>
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="clickRoleTab('inspector', 3, 'joint', 'History')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-clock-rotate-left"></i> Joint Sign</span>
                                        </button>
                                    </li>
                                </ul>
                            </div>
                            <div>
                                <div class="sidebar-group-title">Contacts</div>
                                <ul class="sidebar-nav-list">
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="showToast('Town Council Helpdesk: 6500 0300')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-phone"></i> Emergency Contact</span>
                                        </button>
                                    </li>
                                </ul>
                            </div>
                        </aside>

                        <div class="dashboard-main-panel">
                            <!-- Subview 1: Inspector Home with SENT-BACK QUEUE -->
                            <div id="inspector-sub-home" class="subview-container active">
                                <div class="role-welcome-banner">
                                    <h1>EMS Inspector Field Portal</h1>
                                    <p>Mobile-optimized spot-check dispatch and joint endorsement.</p>
                                </div>

                                <!-- SENT-BACK RECTIFICATION QUEUE (HIGHEST PRIORITY) -->
                                <div class="sent-back-queue-banner">
                                    <h3><i class="fa-solid fa-triangle-exclamation"></i> 1 Sent Back Defect — Action Required</h3>
                                    <p>Estate Manager returned D-0417 for re-inspection following Fujitec rework.</p>
                                    <div class="defect-row-card" style="background:#ffffff; margin-bottom:8px;">
                                        <div class="defect-row-top">
                                            <div>
                                                <h4 style="color:#b91c1c;">(9) ARD & EBOPS Operation</h4>
                                                <p>Blk 559/A Woodlands St 54 • Fujitec Lifts</p>
                                            </div>
                                            <span class="severity-pill major">Re-Inspect</span>
                                        </div>
                                        <div style="font-size:0.7rem; color:#475569; margin:4px 0;">
                                            <strong>Manager Feedback:</strong> Battery pack replaced, but ARD test was not witnessed. Retest on site and sign off.
                                        </div>
                                        <button type="button" class="btn-primary-blue" style="background:#ef4444; width:auto; font-size:0.7rem; margin-top:4px;" onclick="clickRoleTab('inspector', 1, 'checklist', 'New Inspection'); showToast('Opening Form 12b for Blk 559/A!');">
                                            <i class="fa-solid fa-rotate-right"></i> Re-Inspect Now on Site
                                        </button>
                                    </div>
                                </div>

                                <!-- Today's Assigned Digital Checklists Mapped by HDB Block -->
                                <div class="task-header-block">
                                    <h3 style="font-size:0.95rem; font-weight:800; color:#0f2b48; margin-bottom:8px;">Today's Assigned Checklists</h3>
                                    
                                    <div class="defect-row-card" style="border-left:4px solid #10b981;">
                                        <div class="defect-row-top">
                                            <div>
                                                <h4>Blk 554 Lift A (Woodlands St 53)</h4>
                                                <span style="font-size:0.65rem; color:#64748b;">Mitsubishi • Serviced yesterday • Scheduled: 09:00 AM</span>
                                            </div>
                                            <button type="button" class="btn-primary-blue" style="background:#10b981; width:auto; font-size:0.68rem; padding:4px 8px;" onclick="clickRoleTab('inspector', 1, 'checklist', 'New Inspection')">
                                                Start Form 12b
                                            </button>
                                        </div>
                                    </div>

                                    <div class="defect-row-card" style="border-left:4px solid #3b82f6;">
                                        <div class="defect-row-top">
                                            <div>
                                                <h4>Blk 573 Lift C (Woodlands Dr 44)</h4>
                                                <span style="font-size:0.65rem; color:#64748b;">Schindler • Scheduled: 11:30 AM</span>
                                            </div>
                                            <button type="button" class="btn-secondary-outline" style="width:auto; font-size:0.68rem; padding:4px 8px;" onclick="showToast('Checklist loaded for Blk 573')">
                                                Open Checklist
                                            </button>
                                        </div>
                                    </div>

                                    <div class="defect-row-card" style="border-left:4px solid #f59e0b;">
                                        <div class="defect-row-top">
                                            <div>
                                                <h4>Blk 476 Lift 1B (Pasir Ris Dr 6)</h4>
                                                <span style="font-size:0.65rem; color:#64748b;">Fujitec • Scheduled: 02:00 PM</span>
                                            </div>
                                            <button type="button" class="btn-secondary-outline" style="width:auto; font-size:0.68rem; padding:4px 8px;" onclick="showToast('Checklist loaded for Blk 476')">
                                                Open Checklist
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Subview 2: Junxi's 25-Point Checklist -->
                            <div id="inspector-sub-checklist" class="subview-container">
                                <div class="junxi-checklist-header">
                                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                                        <span class="junxi-lift-brand">SBTC • MITSUBISHI</span>
                                        <span class="status-badge" style="background:#fef3c7; color:#d97706;">In Progress</span>
                                    </div>
                                    <h2 style="font-size:1.15rem; font-weight:800; color:#0f2b48;">Blk 554 Lift A - Woodlands St 53</h2>
                                    <p style="font-size:0.72rem; color:#64748b;">Form 12b Spot-Check of Lift Servicing (Junxi's Checklist)</p>
                                </div>

                                <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:10px; margin-bottom:10px; display:flex; justify-content:space-between; font-size:0.75rem;">
                                    <span>Progress: <strong>25 / 25 Items Verified</strong></span>
                                    <span id="junxiDefectSummaryBadge" class="status-badge" style="background:#fee2e2; color:#dc2626;">4 Defects Spotted</span>
                                </div>

                                <div class="checklist-category-pill" style="background:#0263b3; color:#ffffff; padding:7px 12px; border-radius:8px; font-size:0.75rem; font-weight:700; margin-bottom:8px;">
                                    (A) MOTOR ROOM (9 Items)
                                </div>
                                <div id="junxiSectionA_Items"></div>

                                <div class="checklist-category-pill" style="background:#0263b3; color:#ffffff; padding:7px 12px; border-radius:8px; font-size:0.75rem; font-weight:700; margin:10px 0 8px;">
                                    (B) LIFT CAR (8 Items)
                                </div>
                                <div id="junxiSectionB_Items"></div>

                                <div class="checklist-category-pill" style="background:#0263b3; color:#ffffff; padding:7px 12px; border-radius:8px; font-size:0.75rem; font-weight:700; margin:10px 0 8px;">
                                    (C) HOISTWAY & LIFT PIT (8 Items)
                                </div>
                                <div id="junxiSectionC_Items"></div>

                                <div class="signature-card">
                                    <div style="display:flex; justify-content:space-between; font-size:0.74rem; font-weight:700; margin-bottom:4px;">
                                        <span><i class="fa-solid fa-signature"></i> Checked By: Inspector Signature</span>
                                        <button type="button" style="background:none; border:none; color:#ef4444; font-size:0.7rem; cursor:pointer;" id="btnClearInspectorSign">Clear</button>
                                    </div>
                                    <canvas id="canvasInspectorSign" class="signature-canvas" width="380" height="85"></canvas>
                                </div>

                                <button type="button" class="btn-primary-blue" style="margin-top:10px; background:#10b981;" onclick="showToast('Form 12b submitted! Dispatched to Mitsubishi LC.'); clickRoleTab('inspector', 2, 'queue', 'My Inspections');">
                                    <i class="fa-solid fa-paper-plane"></i> Submit Form 12b & Notify Contractor
                                </button>
                            </div>

                            <!-- Subview 3: Today's Queue -->
                            <div id="inspector-sub-queue" class="subview-container">
                                <div class="role-welcome-banner">
                                    <h1>Assigned Lift Inspections</h1>
                                    <p>Spot-checks scheduled across Town Council Divisions.</p>
                                </div>

                                <div class="defect-row-card">
                                    <h4>Blk 573 Lift C - Woodlands Dr 44</h4>
                                    <p style="font-size:0.72rem; color:#64748b;">Schindler Lifts • Scheduled 11:30 AM</p>
                                    <button type="button" class="btn-primary-blue" style="margin-top:6px; font-size:0.72rem; background:#10b981; width:auto;" onclick="showToast('Checklist loaded for Blk 573!')">
                                        Start Spot-Check
                                    </button>
                                </div>
                            </div>

                            <!-- Subview 4: Joint Sign / History -->
                            <div id="inspector-sub-joint" class="subview-container">
                                <div class="role-welcome-banner">
                                    <h1>Joint Endorsement History</h1>
                                    <p>Conduct joint sign-off with contractor following defect rectification.</p>
                                </div>

                                <div class="defect-row-card">
                                    <h4>Blk 554 Lift A - Clearance Sign-off</h4>
                                    <p style="font-size:0.72rem; color:#64748b;">Contractor Ah Seng reported 4 defects rectified.</p>
                                    <button type="button" class="btn-primary-blue" style="margin-top:6px; font-size:0.72rem; background:#10b981; width:auto;" onclick="showToast('Joint Endorsement completed!')">
                                        Verify & Endorse Clearance
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- ============================================================== -->
                <!-- ROLE 4: RESIDENT PORTAL (MATCHING ALL 7 FIGMA SCREENSHOTS)    -->
                <!-- ============================================================== -->
                <div id="view-role-resident" class="screen-view">
                    <div class="dashboard-layout-wrap">
                        <aside class="role-desktop-sidebar resident">
                            <div>
                                <div class="sidebar-group-title">Services</div>
                                <ul class="sidebar-nav-list">
                                    <li class="sidebar-nav-item">
                                        <button type="button" class="active" onclick="clickRoleTab('resident', 0, 'home', 'Home')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-house"></i> Home</span>
                                        </button>
                                    </li>
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="clickRoleTab('resident', 1, 'report', 'Report Issue')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-circle-exclamation"></i> Report Lift Issue</span>
                                        </button>
                                    </li>
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="clickRoleTab('resident', 2, 'my-reports', 'My Reports')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-bullseye"></i> Track Report</span>
                                            <span class="sidebar-item-badge">4</span>
                                        </button>
                                    </li>
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="clickRoleTab('resident', 3, 'notices', 'Notice Board')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-users"></i> My Community</span>
                                        </button>
                                    </li>
                                </ul>
                            </div>
                            <div>
                                <div class="sidebar-group-title">Help & Support</div>
                                <ul class="sidebar-nav-list">
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="openEmergencyModal()">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-phone"></i> Helpline</span>
                                        </button>
                                    </li>
                                    <li class="sidebar-nav-item">
                                        <button type="button" onclick="showToast('FAQs: Lift servicing conducted monthly per BCA Form 12b standard.')">
                                            <span class="sidebar-item-left"><i class="fa-solid fa-circle-question"></i> FAQ</span>
                                        </button>
                                    </li>
                                </ul>
                            </div>
                        </aside>

                        <div class="dashboard-main-panel">
                            <!-- Subview 1: 15 Resident Home (Matching Figma Image 6) -->
                            <div id="resident-sub-home" class="subview-container active">
                                <div class="resident-hero-card">
                                    <h1>Good Morning, Resident Sanjay!! 👋</h1>
                                    <div class="resident-hero-sub">HDB Blk #476 | Pasir Ris Dr 6 (Woodlands Town Council)</div>
                                    
                                    <!-- My Lift Notices (Image 6 top) -->
                                    <div class="resident-notices-section">
                                        <div class="resident-section-header">
                                            <div class="resident-section-title">My Lift Notices</div>
                                            <a href="#" class="resident-view-all-link" onclick="clickRoleTab('resident', 3, 'notices', 'Notice Board'); return false;">View all</a>
                                        </div>
                                        <div class="notice-cards-grid">
                                            <div class="notice-card-item danger-card">
                                                <h4>Lift 1A Closed for Repairs</h4>
                                                <span>Undergoing emergency motor bearing repair</span>
                                            </div>
                                            <div class="notice-card-item warning-card">
                                                <h4>Lift 1B Scheduled Inspection</h4>
                                                <span>Routine servicing today 2:00 PM – 4:00 PM</span>
                                            </div>
                                            <div class="notice-card-item success-card">
                                                <h4>Lift 2B Repaired</h4>
                                                <span>Operational • Door alignment completed</span>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Shortcuts (Image 6 right) -->
                                    <div class="resident-section-title" style="margin-bottom:8px;">Shortcuts</div>
                                    <div class="resident-shortcuts-card">
                                        <button type="button" class="resident-shortcut-btn" onclick="clickRoleTab('resident', 1, 'report', 'Report Issue')">
                                            <div class="shortcut-left">
                                                <div class="shortcut-icon-circle danger"><i class="fa-solid fa-circle-exclamation"></i></div>
                                                <span>Report an Issue</span>
                                            </div>
                                            <i class="fa-solid fa-chevron-right" style="font-size:0.75rem; color:#94a3b8;"></i>
                                        </button>
                                        <button type="button" class="resident-shortcut-btn" onclick="clickRoleTab('resident', 2, 'my-reports', 'My Reports')">
                                            <div class="shortcut-left">
                                                <div class="shortcut-icon-circle info"><i class="fa-solid fa-bullseye"></i></div>
                                                <span>Track your reports</span>
                                            </div>
                                            <i class="fa-solid fa-chevron-right" style="font-size:0.75rem; color:#94a3b8;"></i>
                                        </button>
                                        <button type="button" class="resident-shortcut-btn" onclick="openEmergencyModal()">
                                            <div class="shortcut-left">
                                                <div class="shortcut-icon-circle emergency"><i class="fa-solid fa-phone"></i></div>
                                                <span>Emergency Helpline</span>
                                            </div>
                                            <i class="fa-solid fa-chevron-right" style="font-size:0.75rem; color:#94a3b8;"></i>
                                        </button>
                                    </div>
                                </div>
                            </div>

                            <!-- Subview 2: Report a Lift Issue Form (Matching Figma Images 2, 3, 4, 5, 7) -->
                            <div id="resident-sub-report" class="subview-container">
                                <div class="figma-auth-card" style="padding:20px; margin:0; max-width:100%;">
                                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px;">
                                        <div>
                                            <h2 style="font-size:1.25rem; font-weight:800; color:#0f2b48;">Report a lift issue</h2>
                                            <p style="font-size:0.75rem; color:#64748b;">Tell us about the lift defect so we can resolve it quickly.</p>
                                        </div>
                                        <i class="fa-solid fa-list-check" style="font-size:1.8rem; color:#0263b3;"></i>
                                    </div>

                                    <!-- Alert on missing required fields (Image 6 bottom) -->
                                    <div id="residentFormMissingAlert" class="alert-box danger" style="display:none;">
                                        <i class="fa-solid fa-circle-exclamation"></i>
                                        <span>Please fill in all required fields marked * before submitting.</span>
                                    </div>

                                    <!-- Success banner on submit (Image 3 right) -->
                                    <div id="residentFormSuccessBanner" class="alert-box success" style="display:none;">
                                        <i class="fa-solid fa-circle-check"></i>
                                        <span>Report submitted — a manager will review it and set its priority.</span>
                                    </div>

                                    <form id="formResidentReportDefect" style="display:flex; flex-direction:column; gap:10px;">
                                        <div class="figma-field-group">
                                            <label>Title *</label>
                                            <input type="text" id="resReportTitle" class="figma-input" placeholder="e.g. Lift button not lighting up" value="Lift button malfunctioning" required>
                                        </div>

                                        <div class="figma-field-group">
                                            <label>Description *</label>
                                            <textarea id="resReportDesc" class="figma-input" rows="3" placeholder="Describe the issue in detail and exactly where it is." required>The call button for Lift A at the ground floor lift lobby doesn't light up or respond when pressed. Residents have to wait for someone inside the lift to call it down.</textarea>
                                            <span style="font-size:0.65rem; color:#94a3b8;">Provide as much detail as possible, e.g. Level 3 lift lobby, near Lift A.</span>
                                        </div>

                                        <div class="figma-input-row">
                                            <div class="figma-field-group">
                                                <label>Block *</label>
                                                <select id="resReportBlock" class="figma-input" required>
                                                    <option value="556">556</option>
                                                    <option value="558">558</option>
                                                    <option value="476">476</option>
                                                </select>
                                            </div>
                                            <div class="figma-field-group">
                                                <label>Lift No. *</label>
                                                <select id="resReportLiftNo" class="figma-input" required>
                                                    <option value="Lift A">Lift A</option>
                                                    <option value="Lift B">Lift B</option>
                                                    <option value="Lift 1A">Lift 1A</option>
                                                    <option value="Lift 1B">Lift 1B</option>
                                                </select>
                                            </div>
                                        </div>

                                        <div class="figma-field-group">
                                            <label>Category *</label>
                                            <select id="resReportCategory" class="figma-input" required>
                                                <option value="Electrical">⚡ Electrical</option>
                                                <option value="Structural">🏗️ Structural</option>
                                                <option value="Miscellaneous">🔧 Miscellaneous</option>
                                            </select>
                                            <span style="font-size:0.65rem; color:#94a3b8;">Pick Miscellaneous if you're not sure — a manager will check it</span>
                                        </div>

                                        <button type="button" class="btn-secondary-outline" style="width:auto; font-size:0.72rem; align-self:flex-start;" onclick="captureResidentLocation()">
                                            <i class="fa-solid fa-crosshairs"></i> Capture location
                                        </button>

                                        <!-- Photo Dropzone & Attached Thumbnail (Image 3 left & Image 4) -->
                                        <div class="figma-field-group">
                                            <label>Photos (optional)</label>
                                            <div class="photo-uploader-box" onclick="openPhotoUploadModal()">
                                                <i class="fa-solid fa-image" style="font-size:1.5rem; color:#0263b3; margin-bottom:4px;"></i>
                                                <div><strong>Add photos</strong></div>
                                                <div style="font-size:0.65rem; color:#64748b;">Drag and drop or click to upload • JPG, PNG up to 10MB each — AI scans it for defects</div>
                                            </div>
                                            
                                            <!-- Thumbnail chip -->
                                            <div id="resPhotoAttachedThumb" class="photo-thumbnails-row" style="display:flex;">
                                                <span class="photo-thumb-chip"><i class="fa-solid fa-image"></i> lift_button_panel.jpg (2.4 MB) • 1 photo added</span>
                                            </div>
                                        </div>

                                        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px;">
                                            <button type="button" class="btn-secondary-outline" style="width:auto;" onclick="openDiscardModal()">
                                                Cancel
                                            </button>
                                            <button type="submit" class="btn-primary-blue" style="width:auto;">
                                                <i class="fa-solid fa-paper-plane"></i> Submit issue
                                            </button>
                                        </div>
                                    </form>
                                </div>
                            </div>

                            <!-- Subview 3: Track Report / My Reports (Matching Figma Image 1) -->
                            <div id="resident-sub-my-reports" class="subview-container">
                                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
                                    <div>
                                        <h2 style="font-size:1.25rem; font-weight:800; color:#0f2b48;">My Reports</h2>
                                        <p style="font-size:0.75rem; color:#64748b;">Track the progress of the lift issues you've reported.</p>
                                    </div>
                                    <button type="button" class="btn-primary-blue" style="width:auto; font-size:0.75rem;" onclick="clickRoleTab('resident', 1, 'report', 'Report Issue')">
                                        <i class="fa-solid fa-plus"></i> Report a new issue
                                    </button>
                                </div>

                                <!-- 4 Metrics Cards (Image 1 right) -->
                                <div class="report-track-summary-grid">
                                    <div class="track-stat-card">
                                        <div class="track-stat-icon" style="background:#eff6ff; color:#0263b3;"><i class="fa-regular fa-file-lines"></i></div>
                                        <div class="track-stat-info">
                                            <span class="track-stat-num" id="resTotalSubCount">4</span>
                                            <span class="track-stat-label">Total reports submitted</span>
                                        </div>
                                    </div>
                                    <div class="track-stat-card">
                                        <div class="track-stat-icon" style="background:#fef3c7; color:#d97706;"><i class="fa-regular fa-clock"></i></div>
                                        <div class="track-stat-info">
                                            <span class="track-stat-num">1</span>
                                            <span class="track-stat-label">Waiting for review</span>
                                        </div>
                                    </div>
                                    <div class="track-stat-card">
                                        <div class="track-stat-icon" style="background:#fff7ed; color:#ea580c;"><i class="fa-solid fa-wrench"></i></div>
                                        <div class="track-stat-info">
                                            <span class="track-stat-num">2</span>
                                            <span class="track-stat-label">Review, repairs or testing</span>
                                        </div>
                                    </div>
                                    <div class="track-stat-card">
                                        <div class="track-stat-icon" style="background:#dcfce7; color:#16a34a;"><i class="fa-solid fa-circle-check"></i></div>
                                        <div class="track-stat-info">
                                            <span class="track-stat-num">2</span>
                                            <span class="track-stat-label">Resolved & verified</span>
                                        </div>
                                    </div>
                                </div>

                                <!-- Latest records list (Image 1 left) -->
                                <div class="latest-records-wrap">
                                    <div style="font-size:0.85rem; font-weight:800; color:#0f2b48; margin-bottom:10px;">Latest records</div>
                                    
                                    <div class="latest-record-row" onclick="toggleDefectDrawer('resRecordDetail1')">
                                        <div class="record-row-left">
                                            <h5>REQ-103: Lift B door not closing properly</h5>
                                            <p>Submitted today • Blk 556 Lift B</p>
                                        </div>
                                        <span class="status-badge" style="background:#eff6ff; color:#1d4ed8;">In progress</span>
                                    </div>
                                    <div id="resRecordDetail1" style="display:none; padding:8px; background:#f8fafc; border-radius:6px; font-size:0.7rem; margin-bottom:8px;">
                                        <strong>Progress:</strong> Contractor Kumar arrived on site. Cleaning landing door tracks and adjusting eccentric rollers.
                                    </div>

                                    <div class="latest-record-row" onclick="toggleDefectDrawer('resRecordDetail2')">
                                        <div class="record-row-left">
                                            <h5>REQ-102: Unusual noise at level 8</h5>
                                            <p>Submitted yesterday • Blk 554 Lift A</p>
                                        </div>
                                        <span class="status-badge" style="background:#fef3c7; color:#b45309;">Under review</span>
                                    </div>
                                    <div id="resRecordDetail2" style="display:none; padding:8px; background:#f8fafc; border-radius:6px; font-size:0.7rem; margin-bottom:8px;">
                                        <strong>Progress:</strong> Town Council Estate Manager assigned to Mitsubishi technician for motor bearing check.
                                    </div>

                                    <div class="latest-record-row" onclick="toggleDefectDrawer('resRecordDetail3')">
                                        <div class="record-row-left">
                                            <h5>REQ-101: Lift breakdown follow-up</h5>
                                            <p>Submitted 3 days ago • Blk 556 Lift A</p>
                                        </div>
                                        <span class="status-badge" style="background:#dcfce7; color:#166534;">Resolved</span>
                                    </div>
                                    <div id="resRecordDetail3" style="display:none; padding:8px; background:#f8fafc; border-radius:6px; font-size:0.7rem; margin-bottom:8px;">
                                        <strong>Progress:</strong> Power trip resolved by EMSU. Test run 10 landings verified passed.
                                    </div>
                                </div>
                            </div>

                            <!-- Subview 4: Community Notices & Helpline -->
                            <div id="resident-sub-notices" class="subview-container">
                                <div class="role-welcome-banner">
                                    <h1>Estate Notice Board</h1>
                                    <p>Town Council lift upgrading, servicing schedule, and community alerts.</p>
                                </div>

                                <div class="defect-row-card">
                                    <h4>Lift Modernisation Programme 2026</h4>
                                    <p style="font-size:0.72rem; color:#64748b;">New ARD emergency battery backup installation scheduled for 28 April 2026.</p>
                                </div>
                                <div class="defect-row-card">
                                    <h4>Routine Servicing Notice</h4>
                                    <p style="font-size:0.72rem; color:#64748b;">Monthly servicing for passenger lifts conducted on 4th week of each month.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </main>

            <!-- DYNAMIC ROLE-SPECIFIC BOTTOM NAVIGATION BARS (MOBILE VIEW) -->
            <nav class="role-bottom-nav manager" id="roleBottomNav" style="display:none;"></nav>
        </div>
    </div>

    <!-- MODAL 1: Reopen Defect Modal (History) -->
    <div class="modal-overlay" id="modalReopenDefect">
        <div class="modal-card">
            <h3 style="font-size:1.05rem; font-weight:800; color:#0f2b48; margin-bottom:4px;">Reopen this defect</h3>
            <p style="font-size:0.72rem; color:#64748b; line-height:1.4; margin-bottom:12px;">
                Sends it back to Pending Rectification. Sets a new due date and emails the lift contractor. The sign-off record stays in History.
            </p>
            <div class="figma-field-group">
                <label>Reason for reopening (required)</label>
                <textarea class="figma-input" id="reopenReasonInput" rows="3" placeholder="Enter specific reason for reopening defect..."></textarea>
            </div>
            <div style="display:flex; justify-content:flex-end; gap:8px; margin-top:14px;">
                <button type="button" class="btn-secondary-outline" style="width:auto;" onclick="closeReopenModal()">Cancel</button>
                <button type="button" class="btn-primary-blue" style="width:auto; background:#ef4444;" onclick="submitReopenDefect()">Reopen Defect</button>
            </div>
        </div>
    </div>

    <!-- MODAL 2: Photo Upload Popup Modal (Matching Figma Image 4 right) -->
    <div class="modal-overlay" id="modalUploadPhoto">
        <div class="modal-card" style="max-width:380px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                <h3 style="font-size:1.05rem; font-weight:800; color:#0f2b48;">Upload a photo</h3>
                <button type="button" style="background:none; border:none; font-size:1rem; cursor:pointer;" onclick="closePhotoUploadModal()">&times;</button>
            </div>
            <p style="font-size:0.72rem; color:#64748b; margin-bottom:12px;">Choose a photo from your device to attach to this report.</p>

            <div style="border:1px solid #e2e8f0; border-radius:8px; padding:10px; display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
                <div style="display:flex; align-items:center; gap:8px;">
                    <div style="width:36px; height:36px; background:#eff6ff; border-radius:6px; display:flex; align-items:center; justify-content:center; color:#0263b3;">
                        <i class="fa-solid fa-image"></i>
                    </div>
                    <div>
                        <div style="font-size:0.75rem; font-weight:700; color:#0f2b48;">lift_button_panel.jpg</div>
                        <div style="font-size:0.65rem; color:#64748b;">2.4 MB • Taken today, 1:42 AM</div>
                    </div>
                </div>
                <button type="button" class="btn-primary-blue" style="width:auto; padding:4px 10px; font-size:0.7rem;" onclick="confirmPhotoUpload()">Upload</button>
            </div>
            <div style="display:flex; justify-content:flex-end;">
                <button type="button" class="btn-secondary-outline" style="width:auto;" onclick="closePhotoUploadModal()">Cancel</button>
            </div>
        </div>
    </div>

    <!-- MODAL 3: Discard Report Confirmation Modal (Matching Figma Image 2) -->
    <div class="modal-overlay" id="modalDiscardReport">
        <div class="modal-card" style="max-width:360px; text-align:center;">
            <div style="width:48px; height:48px; border-radius:50%; background:#fffbeb; color:#f59e0b; display:inline-flex; align-items:center; justify-content:center; font-size:1.4rem; margin-bottom:10px;">
                <i class="fa-solid fa-triangle-exclamation"></i>
            </div>
            <h3 style="font-size:1.05rem; font-weight:800; color:#0f2b48; margin-bottom:4px;">Discard this report?</h3>
            <p style="font-size:0.74rem; color:#64748b; line-height:1.4; margin-bottom:16px;">
                The details you've entered will be lost. This can't be undone.
            </p>
            <div style="display:flex; justify-content:center; gap:8px;">
                <button type="button" class="btn-secondary-outline" style="width:auto;" onclick="closeDiscardModal()">Keep editing</button>
                <button type="button" class="btn-primary-blue" style="width:auto; background:#ef4444;" onclick="confirmDiscardReport()">Discard report</button>
            </div>
        </div>
    </div>

    <!-- MODAL 4: CSV Import Modal (Estate Manager) -->
    <div class="modal-overlay" id="modalImportCSV">
        <div class="modal-card" style="max-width:540px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                <h3 style="font-size:1.1rem; font-weight:800; color:#0f2b48;"><i class="fa-solid fa-file-csv" style="color:#10b981;"></i> Bulk Import Maintenance Records</h3>
                <button type="button" style="background:none; border:none; font-size:1.1rem; cursor:pointer;" onclick="closeCsvImportModal()">&times;</button>
            </div>
            <p style="font-size:0.72rem; color:#64748b; margin-bottom:10px;">Upload a CSV file containing defect records. Columns: Block, LiftID, DefectType, Contractor, Severity, DueDate, Status.</p>
            
            <div style="display:flex; gap:8px; margin-bottom:10px;">
                <button type="button" class="btn-secondary-outline" style="font-size:0.7rem; width:auto;" onclick="loadSampleCsvData()">
                    <i class="fa-solid fa-wand-magic-sparkles"></i> Load Sample Maintenance CSV
                </button>
            </div>

            <div class="csv-preview-table-wrap">
                <table class="csv-preview-table">
                    <thead>
                        <tr>
                            <th>Block</th>
                            <th>Lift ID</th>
                            <th>Defect Type</th>
                            <th>Contractor</th>
                            <th>Severity</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody id="csvPreviewTableBody">
                        <tr><td colspan="6" style="text-align:center; color:#94a3b8; padding:16px;">No CSV data loaded yet. Click "Load Sample" or select a file.</td></tr>
                    </tbody>
                </table>
            </div>

            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:12px;">
                <span id="csvValidationStatus" style="font-size:0.7rem; color:#10b981; font-weight:700;"></span>
                <div style="display:flex; gap:8px;">
                    <button type="button" class="btn-secondary-outline" style="width:auto;" onclick="closeCsvImportModal()">Cancel</button>
                    <button type="button" class="btn-primary-blue" id="btnConfirmCsvImport" style="width:auto;" disabled onclick="confirmCsvImport()">Confirm & Import Records</button>
                </div>
            </div>
        </div>
    </div>

    <!-- MODAL 5: Assign Technician Modal (Contractor) -->
    <div class="modal-overlay" id="modalAssignTech">
        <div class="modal-card" style="max-width:380px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                <h3 style="font-size:1.05rem; font-weight:800; color:#0f2b48;">Assign Technician</h3>
                <button type="button" style="background:none; border:none; font-size:1rem; cursor:pointer;" onclick="closeAssignTechModal()">&times;</button>
            </div>
            <form id="formAssignTech" onsubmit="submitAssignTech(event)" style="display:flex; flex-direction:column; gap:10px;">
                <div class="figma-field-group">
                    <label>Select Technician</label>
                    <select class="figma-input" id="selectTechName">
                        <option value="Ah Seng">Ah Seng (Senior Tech • Woodlands)</option>
                        <option value="Kumar">Kumar (Hoistway Specialist)</option>
                        <option value="Wei Ming">Wei Ming (Electrical & ARD Specialist)</option>
                    </select>
                </div>
                <div class="figma-field-group">
                    <label>Select Task</label>
                    <select class="figma-input" id="selectTechTask">
                        <option>Blk 556/B - Wire ropes red dust lubrication</option>
                        <option>Blk 557/B - Controller contactor humming replacement</option>
                        <option>Blk 558/A - Bearing noise acoustic check</option>
                    </select>
                </div>
                <div style="display:flex; justify-content:flex-end; gap:8px; margin-top:6px;">
                    <button type="button" class="btn-secondary-outline" style="width:auto;" onclick="closeAssignTechModal()">Cancel</button>
                    <button type="submit" class="btn-primary-blue" style="width:auto; background:#d97706;">Assign Task</button>
                </div>
            </form>
        </div>
    </div>

    <!-- MODAL 6: Broadcast Community Notice (Contractor / Manager) -->
    <div class="modal-overlay" id="modalBroadcastNotice">
        <div class="modal-card" style="max-width:400px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                <h3 style="font-size:1.05rem; font-weight:800; color:#0f2b48;"><i class="fa-solid fa-bullhorn" style="color:#d97706;"></i> Broadcast Community Notice</h3>
                <button type="button" style="background:none; border:none; font-size:1rem; cursor:pointer;" onclick="closeBroadcastModal()">&times;</button>
            </div>
            <form id="formBroadcastNotice" onsubmit="submitBroadcastNotice(event)" style="display:flex; flex-direction:column; gap:10px;">
                <div class="figma-field-group">
                    <label>Target HDB Block / Zone</label>
                    <select class="figma-input" id="broadcastZone">
                        <option>All Woodlands Blocks (SBTC)</option>
                        <option>Blk 554 & 556 Woodlands St 53</option>
                        <option>Blk 476 Pasir Ris Dr 6</option>
                    </select>
                </div>
                <div class="figma-field-group">
                    <label>Notice Headline</label>
                    <input type="text" class="figma-input" id="broadcastTitle" placeholder="e.g. Scheduled Lift Servicing Notice" value="Notice: Lift A Routine Maintenance on 22 Nov 2026" required>
                </div>
                <div class="figma-field-group">
                    <label>Message Content</label>
                    <textarea class="figma-input" id="broadcastBody" rows="3" required>Lift A will be temporarily halted for routine monthly servicing between 2:00 PM and 4:00 PM. Lift B remains in service.</textarea>
                </div>
                <div style="display:flex; justify-content:flex-end; gap:8px; margin-top:6px;">
                    <button type="button" class="btn-secondary-outline" style="width:auto;" onclick="closeBroadcastModal()">Cancel</button>
                    <button type="submit" class="btn-primary-blue" style="width:auto;">Publish Notice</button>
                </div>
            </form>
        </div>
    </div>

    <!-- MODAL 7: Emergency Helpline Modal (Resident) -->
    <div class="modal-overlay" id="modalEmergencyHelpline">
        <div class="modal-card" style="max-width:380px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                <h3 style="font-size:1.05rem; font-weight:800; color:#b91c1c;"><i class="fa-solid fa-phone-volume"></i> 24/7 Emergency Lift Helpline</h3>
                <button type="button" style="background:none; border:none; font-size:1rem; cursor:pointer;" onclick="closeEmergencyModal()">&times;</button>
            </div>
            <div style="font-size:0.75rem; line-height:1.5; color:#334155; margin-bottom:12px;">
                <div style="background:#fee2e2; padding:10px; border-radius:8px; margin-bottom:8px;">
                    <strong style="color:#991b1b; font-size:0.85rem;">EMSU 24-Hour Hotline: 1800-275-5555</strong>
                    <div style="font-size:0.68rem; color:#7f1d1d; margin-top:2px;">Immediate rescue dispatch for lift entrapments or emergency breakdowns.</div>
                </div>
                <div><strong>Managing Office (Office Hours):</strong> 6500 0300</div>
                <div><strong>Singapore Civil Defence Force (SCDF):</strong> 995</div>
            </div>
            <div style="display:flex; justify-content:flex-end;">
                <button type="button" class="btn-primary-blue" style="width:auto;" onclick="closeEmergencyModal()">Close</button>
            </div>
        </div>
    </div>

    <!-- Toast Notification -->
    <div class="toast-notice" id="toastNotice">
        <i class="fa-solid fa-circle-check"></i>
        <span id="toastMsg">Action completed</span>
    </div>

    <script>
        // Form 12b 25 items for Junxi's checklist
        const CHECKLIST_ITEMS = {
            A: [
                { id: "A1", num: "(1)", text: "Motor room cleanliness - Any debris?", defaultDefect: true, remark: "Unwanted things to remove" },
                { id: "A2", num: "(2)", text: "Cleanliness of traction machine - Any leakage?", defaultDefect: false, remark: "" },
                { id: "A3", num: "(3)", text: "Controller contactors & relays - Any humming?", defaultDefect: false, remark: "" },
                { id: "A4", num: "(4)", text: "Bearings - Any abnormal noise?", defaultDefect: false, remark: "" },
                { id: "A5", num: "(5)", text: "Wire ropes (main rope & governor rope) and sheaves - Any wear or red dust?", defaultDefect: false, remark: "" },
                { id: "A6", num: "(6)", text: "Brake drum & lining - Sign of worn off? Oily?", defaultDefect: false, remark: "" },
                { id: "A7", num: "(7)", text: "Governor Machine - Any abnormal noise?", defaultDefect: false, remark: "" },
                { id: "A8", num: "(8)", text: "Anti Crime device - Functioning?", defaultDefect: false, remark: "" },
                { id: "A9", num: "(9)", text: "ARD & EBOPS - Functioning? Replacement date?", defaultDefect: false, remark: "" }
            ],
            B: [
                { id: "B1", num: "(1)", text: "COB buttons & CPI - Functioning?", defaultDefect: false, remark: "" },
                { id: "B2", num: "(2)", text: "Car Fan & Grille - Any abnormalities?", defaultDefect: true, remark: "Fan grill to clean" },
                { id: "B3", num: "(3)", text: "Car lights & diffuser - Lighted up and clear?", defaultDefect: false, remark: "" },
                { id: "B4", num: "(4)", text: "Car door operation - Any noise?", defaultDefect: false, remark: "" },
                { id: "B5", num: "(5)", text: "Door side gaps - Less than 10mm?", defaultDefect: false, remark: "" },
                { id: "B6", num: "(6)", text: "Sill to sill clearance - Less than 35mm?", defaultDefect: false, remark: "" },
                { id: "B7", num: "(7)", text: "Safety edge & sensor - Functioning?", defaultDefect: false, remark: "" },
                { id: "B8", num: "(8)", text: "Travelling - Any jerkiness?", defaultDefect: false, remark: "" }
            ],
            C: [
                { id: "C1", num: "(1)", text: "Hall buttons & HPI - Functioning?", defaultDefect: false, remark: "" },
                { id: "C2", num: "(2)", text: "All landing door locks adjustment - Any noise?", defaultDefect: false, remark: "" },
                { id: "C3", num: "(3)", text: "All landing door shoes, tracks and eccentric rollers clearance - Any sign of wear and tear?", defaultDefect: false, remark: "" },
                { id: "C4", num: "(4)", text: "All landing door self-closing devices - Self-closing?", defaultDefect: false, remark: "" },
                { id: "C5", num: "(5)", text: "Levelling at each landings - Level?", defaultDefect: false, remark: "" },
                { id: "C6", num: "(6)", text: "Car top safety and cleanliness - Any safety netting?", defaultDefect: true, remark: "Car top oil can to top up" },
                { id: "C7", num: "(7)", text: "All safety switches - Functioning?", defaultDefect: false, remark: "" },
                { id: "C8", num: "(8)", text: "Lift pit cleanliness - Any debris?", defaultDefect: true, remark: "Lift pit to clean" }
            ]
        };

        const ROLE_NAV_BARS = {
            manager: [
                { id: 'm-home', icon: 'fa-house', label: 'Home', view: 'home', active: true },
                { id: 'm-tasks', icon: 'fa-triangle-exclamation', label: 'Defects', view: 'tasks', badge: '5', active: false },
                { id: 'm-res-rep', icon: 'fa-bullhorn', label: 'Residents', view: 'resident-reports', badge: '2', active: false },
                { id: 'm-reports', icon: 'fa-chart-column', label: 'Reports', view: 'reports', active: false },
                { id: 'm-sched', icon: 'fa-bell', label: 'Alerts', view: 'schedule', active: false }
            ],
            contractor: [
                { id: 'c-home', icon: 'fa-chart-pie', label: 'Operations', view: 'home', active: true },
                { id: 'c-rectify', icon: 'fa-wrench', label: 'Active Tasks', view: 'rectify', badge: '4', active: false },
                { id: 'c-awaiting', icon: 'fa-clock-rotate-left', label: 'Sign-off', view: 'awaiting', badge: '1', active: false },
                { id: 'c-history', icon: 'fa-box-archive', label: 'History', view: 'history', active: false }
            ],
            inspector: [
                { id: 'i-home', icon: 'fa-house', label: 'Field Home', view: 'home', active: true },
                { id: 'i-checklist', icon: 'fa-clipboard-check', label: 'Form 12b', view: 'checklist', active: false },
                { id: 'i-queue', icon: 'fa-list-check', label: 'Queue', view: 'queue', badge: '3', active: false },
                { id: 'i-joint', icon: 'fa-clock-rotate-left', label: 'History', view: 'joint', active: false }
            ],
            resident: [
                { id: 'r-home', icon: 'fa-house', label: 'Home', view: 'home', active: true },
                { id: 'r-report', icon: 'fa-circle-exclamation', label: 'Report Issue', view: 'report', active: false },
                { id: 'r-my-rep', icon: 'fa-bullseye', label: 'Track Report', view: 'my-reports', badge: '4', active: false },
                { id: 'r-notices', icon: 'fa-users', label: 'Community', view: 'notices', active: false }
            ]
        };

        let pendingMfaRole = 'inspector';
        let parsedCsvRows = [];

        const screens = {
            welcome: document.getElementById('view-welcome'),
            'org-login': document.getElementById('view-org-login'),
            'org-sso': document.getElementById('view-org-sso'),
            'activate-invite': document.getElementById('view-activate-invite'),
            mfa: document.getElementById('view-mfa'),
            'resident-login': document.getElementById('view-resident-login'),
            'resident-signup': document.getElementById('view-resident-signup'),
            'forgot-pwd': document.getElementById('view-forgot-pwd'),
            'check-email': document.getElementById('view-check-email'),
            'reset-pwd': document.getElementById('view-reset-pwd'),
            'pwd-success': document.getElementById('view-pwd-success'),
            'access-denied': document.getElementById('view-access-denied'),
            'session-expired': document.getElementById('view-session-expired'),
            'task-rework': document.getElementById('view-task-rework'),
            manager: document.getElementById('view-role-manager'),
            contractor: document.getElementById('view-role-contractor'),
            inspector: document.getElementById('view-role-inspector'),
            resident: document.getElementById('view-role-resident')
        };

        document.addEventListener('DOMContentLoaded', () => {
            setupAuthFlows();
            renderJunxiChecklist();
            setupCanvas('canvasInspectorSign', 'btnClearInspectorSign');
            setupCanvas('canvasTechSign', 'btnClearTechSign');
            setupViewToggle();
            setupMfaInputs();
            setupResidentForm();
        });

        function showToast(msg) {
            const toast = document.getElementById('toastNotice');
            const toastMsg = document.getElementById('toastMsg');
            toastMsg.textContent = msg;
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 2600);
        }

        function showScreen(key) {
            Object.values(screens).forEach(s => s && s.classList.remove('active'));
            if (screens[key]) screens[key].classList.add('active');

            const headerBadge = document.getElementById('userHeaderBadge');
            const headerRoleName = document.getElementById('headerRoleName');
            const headerLogoutBtn = document.getElementById('headerLogoutBtn');

            const isAuth = ['welcome', 'org-login', 'org-sso', 'activate-invite', 'mfa', 'resident-login', 'resident-signup', 'forgot-pwd', 'check-email', 'reset-pwd', 'pwd-success', 'access-denied', 'session-expired', 'task-rework'].includes(key);

            if (isAuth) {
                headerBadge.style.display = 'none';
                headerLogoutBtn.style.display = 'none';
                updateRoleBottomNav(null);
            } else {
                headerBadge.style.display = 'flex';
                headerLogoutBtn.style.display = 'block';
                const titles = { manager: 'Estate Manager', contractor: 'Lift Contractor', inspector: 'EMS Inspector', resident: 'Resident' };
                headerRoleName.textContent = titles[key] || key;
                updateRoleBottomNav(key);
            }

            document.querySelectorAll('.role-pill').forEach(p => {
                if (p.dataset.role === key) p.classList.add('active');
                else p.classList.remove('active');
            });
        }

        function startMfaFlow(role, email) {
            pendingMfaRole = role;
            document.getElementById('mfaEmailTarget').textContent = email;
            showScreen('mfa');
            showToast('2-Factor Code sent to ' + email);
        }

        function setupMfaInputs() {
            const boxes = document.querySelectorAll('.mfa-digit-box');
            boxes.forEach((box, i) => {
                box.addEventListener('input', () => {
                    if (box.value.length === 1 && i < boxes.length - 1) {
                        boxes[i + 1].focus();
                    }
                });
                box.addEventListener('keydown', (e) => {
                    if (e.key === 'Backspace' && !box.value && i > 0) {
                        boxes[i - 1].focus();
                    }
                });
            });
        }

        function updateRoleBottomNav(role) {
            const nav = document.getElementById('roleBottomNav');
            if (!role || !ROLE_NAV_BARS[role]) {
                nav.style.display = 'none';
                return;
            }

            nav.style.display = 'flex';
            nav.className = `role-bottom-nav ${role}`;
            const tabs = ROLE_NAV_BARS[role];

            nav.innerHTML = tabs.map((tab, idx) => `
                <button type="button" class="nav-tab-item ${tab.active ? 'active' : ''}" onclick="clickRoleTab('${role}', ${idx}, '${tab.view}', '${tab.label}')">
                    <i class="fa-solid ${tab.icon}"></i>
                    <span>${tab.label}</span>
                    ${tab.badge ? `<span class="nav-badge">${tab.badge}</span>` : ''}
                </button>
            `).join('');
        }

        function clickRoleTab(role, tabIdx, viewName, label) {
            if (ROLE_NAV_BARS[role]) {
                ROLE_NAV_BARS[role].forEach((t, i) => t.active = (i === tabIdx));
                updateRoleBottomNav(role);
            }

            const sidebarBtns = document.querySelectorAll(`.role-desktop-sidebar.${role} .sidebar-nav-item button`);
            sidebarBtns.forEach((btn, i) => {
                if (i === tabIdx) btn.classList.add('active');
                else btn.classList.remove('active');
            });

            if (role === 'manager') switchManagerSubView(viewName);
            if (role === 'contractor') switchContractorSubView(viewName);
            if (role === 'inspector') switchInspectorSubView(viewName);
            if (role === 'resident') switchResidentSubView(viewName);

            showToast(`${label} view loaded`);
        }

        function switchManagerSubView(sub) {
            document.querySelectorAll('#view-role-manager .subview-container').forEach(c => c.classList.remove('active'));
            const target = document.getElementById(`manager-sub-${sub}`);
            if (target) target.classList.add('active');
        }

        function switchContractorSubView(sub) {
            document.querySelectorAll('#view-role-contractor .subview-container').forEach(c => c.classList.remove('active'));
            const target = document.getElementById(`contractor-sub-${sub}`);
            if (target) target.classList.add('active');
        }

        function switchInspectorSubView(sub) {
            document.querySelectorAll('#view-role-inspector .subview-container').forEach(c => c.classList.remove('active'));
            const target = document.getElementById(`inspector-sub-${sub}`);
            if (target) target.classList.add('active');
        }

        function switchResidentSubView(sub) {
            document.querySelectorAll('#view-role-resident .subview-container').forEach(c => c.classList.remove('active'));
            const target = document.getElementById(`resident-sub-${sub}`);
            if (target) target.classList.add('active');
        }

        // ==============================================================
        // DEFECT DRAWER ACCORDION (ALLOWS ALL DEFECTS TO OPEN)
        // ==============================================================
        function toggleDefectDrawer(drawerId) {
            const drawer = document.getElementById(drawerId);
            if (!drawer) return;
            const isHidden = drawer.style.display === 'none' || drawer.style.display === '';
            drawer.style.display = isHidden ? 'block' : 'none';
        }

        function signOffDefect(defectId, cardId, title) {
            showToast(`Signed off & endorsed ${defectId}: ${title}! Moved to History.`);
            const card = document.getElementById(cardId);
            if (card) {
                card.style.opacity = '0.5';
                setTimeout(() => {
                    card.style.display = 'none';
                    // Update counters
                    let activeCount = parseInt(document.getElementById('countActivePill').textContent) || 5;
                    if (activeCount > 1) {
                        activeCount--;
                        document.getElementById('countActivePill').textContent = activeCount;
                        document.getElementById('managerDefectsBadge').textContent = activeCount;
                        document.getElementById('homeActiveDefectsCount').textContent = activeCount + ' Items';
                    }
                    let histCount = parseInt(document.getElementById('countHistoryPill').textContent) || 2;
                    histCount++;
                    document.getElementById('countHistoryPill').textContent = histCount;
                }, 400);
            }
        }

        // ==============================================================
        // TABS: ACTIVE vs AWAITING SIGN-OFF vs HISTORY (DISTINCT DATA)
        // ==============================================================
        function filterManagerTasks(filterType) {
            document.querySelectorAll('.task-tab-pill').forEach(p => p.classList.remove('active'));
            
            const panelActive = document.getElementById('panelActiveDefects');
            const panelAwaiting = document.getElementById('panelAwaitingDefects');
            const panelHistory = document.getElementById('panelHistoryDefects');

            panelActive.style.display = 'none';
            panelAwaiting.style.display = 'none';
            panelHistory.style.display = 'none';

            if (filterType === 'all') {
                document.getElementById('tabBtnActive').classList.add('active');
                panelActive.style.display = 'block';
                showToast('Showing all active defects');
            } else if (filterType === 'awaiting') {
                document.getElementById('tabBtnAwaiting').classList.add('active');
                panelAwaiting.style.display = 'block';
                showToast('Showing defects awaiting final endorsement');
            } else if (filterType === 'history') {
                document.getElementById('tabBtnHistory').classList.add('active');
                panelHistory.style.display = 'block';
                showToast('Showing historical signed-off records');
            }
        }

        function filterManagerTasksByCompany(company) {
            const cards = document.querySelectorAll('#panelActiveDefects .defect-row-card');
            cards.forEach(card => {
                if (company === 'all' || card.textContent.includes(company)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
            showToast(`Filtering by lift company: ${company}`);
        }

        // ==============================================================
        // CSV EXPORT FEATURE (REAL BROWSER DOWNLOAD)
        // ==============================================================
        function exportDefectsToCSV() {
            const csvRows = [
                ["DefectID", "Block", "LiftID", "Category", "Problem", "Contractor", "Severity", "SpotCheckDate", "DueDate", "Status"],
                ["D-0412", "556", "Lift A", "Motor Room", "Motor room cleanliness - debris", "Mitsubishi", "Minor", "28/03/2026", "11/04/2026", "Pending Rectification"],
                ["D-0413", "556", "Lift B", "Motor Room", "Wire ropes & sheaves red dust", "Mitsubishi", "Major", "28/03/2026", "10/04/2026", "In Progress"],
                ["D-0414", "557", "Lift B", "Motor Room", "Controller contactors humming", "Schindler", "Major", "28/03/2026", "04/04/2026", "Overdue"],
                ["D-0415", "558", "Lift A", "Motor Room", "Bearings abnormal noise", "KONE", "Minor", "28/03/2026", "11/04/2026", "Pending Rectification"],
                ["D-0417", "559", "Lift A", "Motor Room", "ARD & EBOPS testing date", "Fujitec", "Major", "28/03/2026", "04/04/2026", "Awaiting Sign-off"],
                ["D-0391", "556", "Lift A", "Motor Room", "Cleanliness of traction machine", "Mitsubishi", "Minor", "14/03/2026", "02/04/2026", "Signed Off"],
                ["D-0388", "554", "Lift B", "Hoistway", "Landing door lock adjustment", "Schindler", "Minor", "01/03/2026", "14/03/2026", "Signed Off"]
            ];

            let csvContent = "data:text/csv;charset=utf-8," + csvRows.map(e => e.map(cell => `"${cell}"`).join(",")).join("\n");
            let encodedUri = encodeURI(csvContent);
            let link = document.createElement("a");
            link.setAttribute("href", encodedUri);
            link.setAttribute("download", "BEAP_Lift_Maintenance_Logs.csv");
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            showToast('Downloaded BEAP_Lift_Maintenance_Logs.csv');
        }

        // ==============================================================
        // CSV IMPORT FEATURE (MODAL + CLIENT PREVIEW & VALIDATION)
        // ==============================================================
        function openCsvImportModal() {
            document.getElementById('modalImportCSV').classList.add('show');
        }

        function closeCsvImportModal() {
            document.getElementById('modalImportCSV').classList.remove('show');
        }

        function loadSampleCsvData() {
            parsedCsvRows = [
                { block: "560", lift: "Lift A", defect: "Landing door self-closing device stuck", contractor: "Mitsubishi", severity: "Major", status: "Valid" },
                { block: "561", lift: "Lift B", defect: "Car fan rattling noise level 6", contractor: "Fujitec", severity: "Minor", status: "Valid" },
                { block: "562", lift: "Lift A", defect: "Sill to sill gap exceeding 35mm", contractor: "Schindler", severity: "Major", status: "Valid" }
            ];

            const tbody = document.getElementById('csvPreviewTableBody');
            tbody.innerHTML = parsedCsvRows.map(r => `
                <tr>
                    <td><strong>Blk ${r.block}</strong></td>
                    <td>${r.lift}</td>
                    <td>${r.defect}</td>
                    <td>${r.contractor}</td>
                    <td><span class="severity-pill ${r.severity.toLowerCase()}">${r.severity}</span></td>
                    <td style="color:#10b981; font-weight:700;">● ${r.status}</td>
                </tr>
            `).join('');

            document.getElementById('csvValidationStatus').textContent = `3 records validated successfully.`;
            document.getElementById('btnConfirmCsvImport').disabled = false;
        }

        function confirmCsvImport() {
            closeCsvImportModal();
            showToast(`Imported ${parsedCsvRows.length} maintenance records into Active Tasks!`);
            let count = parseInt(document.getElementById('countActivePill').textContent) || 5;
            count += parsedCsvRows.length;
            document.getElementById('countActivePill').textContent = count;
            document.getElementById('managerDefectsBadge').textContent = count;
        }

        // ==============================================================
        // CONTRACTOR MASTER TABLE FILTER & DRILLDOWN
        // ==============================================================
        function filterContractorMasterTable() {
            const query = (document.getElementById('contractorTaskSearch').value || '').toLowerCase();
            const zone = document.getElementById('contractorZoneSelect').value;
            const sev = document.getElementById('contractorSeveritySelect').value;

            document.querySelectorAll('#contractorMasterTableList .contractor-task-item').forEach(item => {
                const text = item.textContent.toLowerCase();
                const itemZone = item.dataset.zone;
                const itemSev = item.dataset.severity;

                const matchQuery = !query || text.includes(query);
                const matchZone = zone === 'all' || itemZone === zone;
                const matchSev = sev === 'all' || itemSev === sev;

                item.style.display = (matchQuery && matchZone && matchSev) ? 'block' : 'none';
            });
        }

        function openAssignTechModal() {
            document.getElementById('modalAssignTech').classList.add('show');
        }
        function closeAssignTechModal() {
            document.getElementById('modalAssignTech').classList.remove('show');
        }
        function submitAssignTech(e) {
            e.preventDefault();
            const tech = document.getElementById('selectTechName').value;
            closeAssignTechModal();
            showToast(`Task successfully assigned to ${tech}!`);
        }

        function openBroadcastModal() {
            document.getElementById('modalBroadcastNotice').classList.add('show');
        }
        function closeBroadcastModal() {
            document.getElementById('modalBroadcastNotice').classList.remove('show');
        }
        function submitBroadcastNotice(e) {
            e.preventDefault();
            const title = document.getElementById('broadcastTitle').value;
            closeBroadcastModal();
            showToast(`Notice published to Resident Notice Board: "${title}"`);
        }

        // ==============================================================
        // RESIDENT SECTION FORMS & MODALS (MATCHING 7 FIGMA IMAGES)
        // ==============================================================
        function setupResidentForm() {
            const form = document.getElementById('formResidentReportDefect');
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                const title = document.getElementById('resReportTitle').value.trim();
                const desc = document.getElementById('resReportDesc').value.trim();
                const alertMissing = document.getElementById('residentFormMissingAlert');
                const bannerSuccess = document.getElementById('residentFormSuccessBanner');

                if (!title || !desc) {
                    alertMissing.style.display = 'flex';
                    bannerSuccess.style.display = 'none';
                    return;
                }

                alertMissing.style.display = 'none';
                bannerSuccess.style.display = 'flex';
                showToast('Your Report has been Submitted! View report >');

                // Increment resident report counters
                let total = parseInt(document.getElementById('resTotalSubCount').textContent) || 4;
                document.getElementById('resTotalSubCount').textContent = total + 1;

                setTimeout(() => {
                    clickRoleTab('resident', 2, 'my-reports', 'Track Report');
                }, 1600);
            });
        }

        function captureResidentLocation() {
            const block = document.getElementById('resReportBlock').value;
            const lift = document.getElementById('resReportLiftNo').value;
            showToast(`GPS Location Captured: Blk ${block} Woodlands St 53 (Near ${lift})`);
        }

        function openPhotoUploadModal() {
            document.getElementById('modalUploadPhoto').classList.add('show');
        }
        function closePhotoUploadModal() {
            document.getElementById('modalUploadPhoto').classList.remove('show');
        }
        function confirmPhotoUpload() {
            closePhotoUploadModal();
            document.getElementById('resPhotoAttachedThumb').style.display = 'flex';
            showToast('Photo has been uploaded! lift_button_panel.jpg was attached.');
        }

        function openDiscardModal() {
            document.getElementById('modalDiscardReport').classList.add('show');
        }
        function closeDiscardModal() {
            document.getElementById('modalDiscardReport').classList.remove('show');
        }
        function confirmDiscardReport() {
            closeDiscardModal();
            document.getElementById('formResidentReportDefect').reset();
            clickRoleTab('resident', 0, 'home', 'Home');
            showToast('Report draft discarded.');
        }

        function openEmergencyModal() {
            document.getElementById('modalEmergencyHelpline').classList.add('show');
        }
        function closeEmergencyModal() {
            document.getElementById('modalEmergencyHelpline').classList.remove('show');
        }

        // ==============================================================
        // REOPEN DEFECT MODAL (HISTORY)
        // ==============================================================
        function openReopenModal(defectTitle) {
            document.getElementById('modalReopenDefect').classList.add('show');
            document.getElementById('reopenReasonInput').value = '';
        }
        function closeReopenModal() {
            document.getElementById('modalReopenDefect').classList.remove('show');
        }
        function submitReopenDefect() {
            const reason = document.getElementById('reopenReasonInput').value.trim();
            if (!reason) {
                alert('Please enter a reason for reopening this defect.');
                return;
            }
            closeReopenModal();
            showToast('Defect reopened! Returned to Pending Rectification.');
            clickRoleTab('manager', 1, 'tasks', 'Major Defects');
        }

        // ==============================================================
        // AUTHENTICATION FLOWS (ZELEN FIGMA)
        // ==============================================================
        function setupAuthFlows() {
            document.getElementById('btnGoResidentLogin').addEventListener('click', () => showScreen('resident-login'));
            document.getElementById('btnGoOrgLogin').addEventListener('click', () => showScreen('org-login'));
            document.getElementById('linkBackWelcomeFromOrg').addEventListener('click', (e) => { e.preventDefault(); showScreen('welcome'); });
            document.getElementById('linkBackWelcomeFromResident').addEventListener('click', (e) => { e.preventDefault(); showScreen('welcome'); });

            document.getElementById('linkActivateAccount').addEventListener('click', (e) => { e.preventDefault(); showScreen('activate-invite'); });
            document.getElementById('formVerifyInvitation').addEventListener('submit', (e) => {
                e.preventDefault();
                startMfaFlow('inspector', document.getElementById('inputInviteEmail').value);
            });
            document.getElementById('btnToggleInvalidInviteDemo').addEventListener('click', () => {
                const errBox = document.getElementById('inviteErrorBox');
                const errNote = document.getElementById('inviteCodeErrorNote');
                const input = document.getElementById('inputInviteCode');
                const isShowing = errBox.style.display === 'flex';
                errBox.style.display = isShowing ? 'none' : 'flex';
                errNote.style.display = isShowing ? 'none' : 'block';
                input.classList.toggle('is-invalid', !isShowing);
                if (!isShowing) input.value = 'EMS-0000-XXXX';
            });

            document.querySelectorAll('.role-pill').forEach(btn => {
                btn.addEventListener('click', () => showScreen(btn.dataset.role));
            });

            document.getElementById('formOrgLogin').addEventListener('submit', (e) => {
                e.preventDefault();
                showScreen('org-sso');
            });

            document.getElementById('formOrgSSOSubmit').addEventListener('submit', (e) => {
                e.preventDefault();
                startMfaFlow('inspector', document.getElementById('ssoOrgEmail').value);
            });
            document.getElementById('btnCancelSSO').addEventListener('click', () => showScreen('org-login'));

            document.getElementById('formMfaVerify').addEventListener('submit', (e) => {
                e.preventDefault();
                showScreen(pendingMfaRole);
                showToast(`2FA Verified! Signed in as ${pendingMfaRole.toUpperCase()}`);
            });
            document.getElementById('btnCancelMfa').addEventListener('click', () => showScreen('org-login'));
            document.getElementById('linkResendMfaCode').addEventListener('click', (e) => {
                e.preventDefault();
                showToast('New 6-digit verification code sent to ' + document.getElementById('mfaEmailTarget').textContent);
            });
            document.getElementById('btnToggleMfaExpiredDemo').addEventListener('click', () => {
                const box = document.getElementById('mfaExpiredAlert');
                const isShowing = box.style.display === 'flex';
                box.style.display = isShowing ? 'none' : 'flex';
                document.querySelectorAll('.mfa-digit-box').forEach(b => b.classList.toggle('is-invalid', !isShowing));
            });

            document.getElementById('formResidentLogin').addEventListener('submit', (e) => {
                e.preventDefault();
                showScreen('resident');
                showToast('Welcome back, Resident!');
            });

            document.getElementById('btnGoResidentSignUp').addEventListener('click', () => showScreen('resident-signup'));
            document.getElementById('linkBackResidentLogin').addEventListener('click', (e) => { e.preventDefault(); showScreen('resident-login'); });
            document.getElementById('formResidentSignUp').addEventListener('submit', (e) => {
                e.preventDefault();
                showScreen('resident');
                showToast('Account Created! Welcome to Resident Portal.');
            });

            document.getElementById('linkGoForgotPw').addEventListener('click', (e) => { e.preventDefault(); showScreen('forgot-pwd'); });
            document.getElementById('linkBackLoginFromForgot').addEventListener('click', (e) => { e.preventDefault(); showScreen('resident-login'); });
            document.getElementById('formForgotPwd').addEventListener('submit', (e) => {
                e.preventDefault();
                showScreen('check-email');
            });

            document.getElementById('btnOpenResetLinkDemo').addEventListener('click', () => showScreen('reset-pwd'));
            document.getElementById('btnBackLoginFromCheckEmail').addEventListener('click', () => showScreen('resident-login'));

            document.getElementById('formResetPasswordSubmit').addEventListener('submit', (e) => {
                e.preventDefault();
                showScreen('pwd-success');
            });
            document.getElementById('linkBackLoginFromReset').addEventListener('click', (e) => { e.preventDefault(); showScreen('resident-login'); });
            document.getElementById('btnBackToLoginAfterSuccess').addEventListener('click', () => showScreen('resident-login'));

            document.getElementById('headerLogoutBtn').addEventListener('click', () => showScreen('welcome'));

            bindPwToggle('btnToggleResidentPw', 'inputResidentPw');
            bindPwToggle('btnToggleSsoPw', 'inputSsoPw');
            bindPwToggle('btnToggleNewPw', 'inputNewPw');
            bindPwToggle('btnToggleConfirmPw', 'inputConfirmPw');
        }

        function bindPwToggle(btnId, inputId) {
            const btn = document.getElementById(btnId);
            const input = document.getElementById(inputId);
            if (!btn || !input) return;
            btn.addEventListener('click', () => {
                if (input.type === 'password') {
                    input.type = 'text';
                    btn.textContent = 'Hide';
                } else {
                    input.type = 'password';
                    btn.textContent = 'Show';
                }
            });
        }

        // ==============================================================
        // JUNXI'S 25-POINT FORM 12b CHECKLIST
        // ==============================================================
        function renderJunxiChecklist() {
            renderJunxiCategory('A', 'junxiSectionA_Items');
            renderJunxiCategory('B', 'junxiSectionB_Items');
            renderJunxiCategory('C', 'junxiSectionC_Items');
        }

        function renderJunxiCategory(catKey, containerId) {
            const container = document.getElementById(containerId);
            const items = CHECKLIST_ITEMS[catKey];

            container.innerHTML = items.map(item => `
                <div class="junxi-item-card ${item.defaultDefect ? 'is-defect' : 'is-pass'}" id="card-${item.id}">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:8px;">
                        <div style="font-size:0.76rem; font-weight:600; flex:1; line-height:1.35;">
                            <span style="color:#0263b3; font-weight:800;">${item.num}</span> ${item.text}
                        </div>
                        <div class="junxi-segmented-group">
                            <button type="button" class="junxi-segmented-btn pass ${!item.defaultDefect ? 'selected' : ''}" onclick="toggleCheckItem('${item.id}', 'pass')">
                                <i class="fa-solid fa-check"></i> Pass
                            </button>
                            <button type="button" class="junxi-segmented-btn defect ${item.defaultDefect ? 'selected' : ''}" onclick="toggleCheckItem('${item.id}', 'defect')">
                                <i class="fa-solid fa-xmark"></i> Defect
                            </button>
                        </div>
                    </div>

                    <div class="junxi-defect-expansion">
                        <div style="display:flex; flex-wrap:wrap; gap:4px;">
                            <span style="font-size:0.62rem; color:#64748b;">Quick Remark:</span>
                            <span class="junxi-chip-btn" onclick="applyRemark('${item.id}', 'Unwanted debris to remove')">Debris to remove</span>
                            <span class="junxi-chip-btn" onclick="applyRemark('${item.id}', 'Fan grill to clean')">Fan grill</span>
                            <span class="junxi-chip-btn" onclick="applyRemark('${item.id}', 'Oil can to top up')">Oil top-up</span>
                        </div>
                        <input type="text" class="figma-input" id="remark-${item.id}" value="${item.remark || ''}" placeholder="Enter defect remarks..." style="font-size:0.72rem; padding:6px 10px;">

                        <div class="junxi-photo-rule-box">
                            <span><i class="fa-solid fa-camera"></i> Evidence Photo (&lt;100KB Limit):</span>
                            <button type="button" class="btn-secondary-outline" style="padding:2px 6px; font-size:0.66rem; width:auto;" onclick="showToast('Photo attached (72 KB) - Validated')">
                                <i class="fa-solid fa-upload"></i> Attach (72 KB)
                            </button>
                        </div>
                    </div>
                </div>
            `).join('');
        }

        function toggleCheckItem(id, status) {
            const card = document.getElementById(`card-${id}`);
            const passBtn = card.querySelector('.junxi-segmented-btn.pass');
            const defectBtn = card.querySelector('.junxi-segmented-btn.defect');

            if (status === 'pass') {
                card.classList.remove('is-defect');
                card.classList.add('is-pass');
                passBtn.classList.add('selected');
                defectBtn.classList.remove('selected');
            } else {
                card.classList.remove('is-pass');
                card.classList.add('is-defect');
                defectBtn.classList.add('selected');
                passBtn.classList.remove('selected');
            }
            updateChecklistCount();
        }

        function applyRemark(id, txt) {
            document.getElementById(`remark-${id}`).value = txt;
        }

        function updateChecklistCount() {
            const count = document.querySelectorAll('.junxi-item-card.is-defect').length;
            const badge = document.getElementById('junxiDefectSummaryBadge');
            badge.textContent = `${count} Defects Spotted`;
            badge.style.background = count > 0 ? '#fee2e2' : '#dcfce7';
            badge.style.color = count > 0 ? '#dc2626' : '#15803d';
        }

        function setupCanvas(canvasId, clearBtnId) {
            const canvas = document.getElementById(canvasId);
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            let drawing = false;

            ctx.lineWidth = 2.2;
            ctx.lineCap = 'round';
            ctx.strokeStyle = '#0f2b48';

            function getPos(e) {
                const rect = canvas.getBoundingClientRect();
                const x = (e.clientX || (e.touches && e.touches[0].clientX)) - rect.left;
                const y = (e.clientY || (e.touches && e.touches[0].clientY)) - rect.top;
                return { x, y };
            }

            canvas.addEventListener('mousedown', (e) => {
                drawing = true;
                const p = getPos(e);
                ctx.beginPath();
                ctx.moveTo(p.x, p.y);
            });
            canvas.addEventListener('mousemove', (e) => {
                if (!drawing) return;
                const p = getPos(e);
                ctx.lineTo(p.x, p.y);
                ctx.stroke();
            });
            window.addEventListener('mouseup', () => drawing = false);

            canvas.addEventListener('touchstart', (e) => {
                e.preventDefault();
                drawing = true;
                const p = getPos(e);
                ctx.beginPath();
                ctx.moveTo(p.x, p.y);
            }, { passive: false });

            canvas.addEventListener('touchmove', (e) => {
                e.preventDefault();
                if (!drawing) return;
                const p = getPos(e);
                ctx.lineTo(p.x, p.y);
                ctx.stroke();
            }, { passive: false });

            window.addEventListener('touchend', () => drawing = false);

            document.getElementById(clearBtnId).addEventListener('click', () => {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
            });
        }

        function setupViewToggle() {
            const btnM = document.getElementById('btnViewMobile');
            const btnD = document.getElementById('btnViewDesktop');
            const wrap = document.getElementById('appWrapper');

            btnM.addEventListener('click', () => {
                btnM.classList.add('active');
                btnD.classList.remove('active');
                wrap.classList.remove('desktop-mode');
            });
            btnD.addEventListener('click', () => {
                btnD.classList.add('active');
                btnM.classList.remove('active');
                wrap.classList.add('desktop-mode');
            });
        }
    </script>
</body>
</html>
'''

target_path = r"C:\Users\User\.gemini\antigravity\scratch\beap-lift-servicing\index.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated index.html successfully. Size:", os.path.getsize(target_path))
